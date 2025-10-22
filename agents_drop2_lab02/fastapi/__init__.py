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
from typing import Any, Callable, Dict, Optional


@dataclass
class _Route:
    method: str
    path: str
    handler: Callable[..., Any]
    response_model: Optional[type] = None


class FastAPI:
    """Tiny substitute for :class:`fastapi.FastAPI` used in the tests."""

    def __init__(self, title: str | None = None, description: str | None = None):
        self.title = title
        self.description = description
        self._routes: Dict[str, Dict[str, _Route]] = {"GET": {}, "POST": {}}

    def _add_route(self, method: str, path: str, func: Callable[..., Any], response_model: Optional[type]):
        self._routes[method][path] = _Route(method, path, func, response_model)
        return func

    def get(self, path: str, response_model: Optional[type] = None):
        def decorator(func: Callable[..., Any]):
            return self._add_route("GET", path, func, response_model)

        return decorator

    def post(self, path: str, response_model: Optional[type] = None):
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

    def _handle_request(self, method: str, path: str, payload: Optional[Dict[str, Any]] = None):
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

        if inspect.iscoroutinefunction(handler):
            result = asyncio.run(handler(*bound_args, **kwargs))
        else:
            result = handler(*bound_args, **kwargs)

        model = route.response_model
        if (
            isinstance(model, type)
            and hasattr(model, "model_validate")
            and not isinstance(result, model)
        ):
            result = model.model_validate(result)

        return result


__all__ = ["FastAPI"]
