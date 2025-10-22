"""Minimal FastAPI-compatible stubs used for the lab's unit tests.

This module mimics a *very* small portion of FastAPI's surface needed by the
exercises.  It supports registering ``get`` and ``post`` routes and invoking
handlers synchronously through the accompanying :mod:`fastapi.testclient`
implementation.
"""
from __future__ import annotations

import asyncio
import inspect
from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional, Tuple, get_args, get_origin


@dataclass
class _Route:
    method: str
    path: str
    handler: Callable[..., Any]
    response_model: Any = None


class HTTPException(Exception):
    """Exception type mimicking :class:`fastapi.HTTPException`."""

    def __init__(self, status_code: int, detail: Any):
        super().__init__(detail)
        self.status_code = status_code
        self.detail = detail


class FastAPI:
    """Tiny substitute for :class:`fastapi.FastAPI` used in the tests."""

    def __init__(self, title: str | None = None, description: str | None = None):
        self.title = title
        self.description = description
        self._routes: Dict[str, Dict[str, _Route]] = {"GET": {}, "POST": {}}

    def _add_route(self, method: str, path: str, func: Callable[..., Any], response_model: Any):
        self._routes[method][path] = _Route(method, path, func, response_model)
        return func

    def get(self, path: str, response_model: Any = None):
        def decorator(func: Callable[..., Any]):
            return self._add_route("GET", path, func, response_model)

        return decorator

    def post(self, path: str, response_model: Any = None):
        def decorator(func: Callable[..., Any]):
            return self._add_route("POST", path, func, response_model)

        return decorator

    def _resolve_argument(
        self,
        parameter: inspect.Parameter,
        annotation: Any,
        payload: Dict[str, Any],
    ) -> Any:
        value = payload.get(parameter.name, inspect.Signature.empty)

        if annotation is inspect.Signature.empty:
            annotation = None

        if annotation is not None and hasattr(annotation, "model_validate"):
            source = payload if value is inspect.Signature.empty else value
            return annotation.model_validate(source)

        if value is inspect.Signature.empty:
            if parameter.default is not inspect.Signature.empty:
                return parameter.default
            return payload

        if annotation in {str, int, float, bool}:
            return annotation(value)

        if callable(annotation) and annotation not in {dict, list, set, tuple}:
            try:
                return annotation(value)
            except TypeError:
                pass

        return value

    def _apply_response_model(self, model: Any, result: Any) -> Any:
        if model is None:
            return result

        if hasattr(model, "model_validate"):
            return model.model_validate(result)

        origin = get_origin(model)
        if origin in (list, tuple, set):
            (item_model,) = get_args(model) or (None,)
            iterable = result or []
            return type(iterable)(
                self._apply_response_model(item_model, item) for item in iterable
            )

        if origin in (dict,):
            key_model, value_model = get_args(model) or (None, None)
            return {
                self._apply_response_model(key_model, key):
                    self._apply_response_model(value_model, value)
                for key, value in (result or {}).items()
            }

        return result

    def _handle_request(self, method: str, path: str, payload: Optional[Dict[str, Any]] = None) -> Tuple[int, Any]:
        if method not in self._routes or path not in self._routes[method]:
            raise ValueError(f"No route registered for {method} {path}")

        route = self._routes[method][path]
        handler = route.handler

        bound_args = []
        kwargs: Dict[str, Any] = {}
        sig = inspect.signature(handler)
        payload_data = payload or {}

        for parameter in sig.parameters.values():
            argument = self._resolve_argument(parameter, parameter.annotation, payload_data)

            if parameter.kind in (
                inspect.Parameter.POSITIONAL_ONLY,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
            ):
                bound_args.append(argument)
            elif parameter.kind == inspect.Parameter.KEYWORD_ONLY:
                kwargs[parameter.name] = argument
            elif parameter.kind == inspect.Parameter.VAR_POSITIONAL:
                if isinstance(argument, (list, tuple)):
                    bound_args.extend(argument)
                else:
                    bound_args.append(argument)
            elif parameter.kind == inspect.Parameter.VAR_KEYWORD:
                if isinstance(argument, dict):
                    kwargs.update(argument)

        try:
            if inspect.iscoroutinefunction(handler):
                coro = handler(*bound_args, **kwargs)
                try:
                    loop = asyncio.get_running_loop()
                except RuntimeError:
                    result = asyncio.run(coro)
                else:
                    if loop.is_running():
                        new_loop = asyncio.new_event_loop()
                        try:
                            result = new_loop.run_until_complete(coro)
                        finally:
                            new_loop.close()
                    else:
                        result = loop.run_until_complete(coro)
            else:
                result = handler(*bound_args, **kwargs)
        except HTTPException as exc:
            return exc.status_code, {"detail": exc.detail}

        status_code = 200
        payload = result

        if isinstance(result, tuple) and len(result) == 2 and isinstance(result[1], int):
            payload, status_code = result

        payload = self._apply_response_model(route.response_model, payload)

        return status_code, payload


__all__ = ["FastAPI", "HTTPException"]
