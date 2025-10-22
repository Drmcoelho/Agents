"""Minimal FastAPI-compatible stubs used for the lab's unit tests.

This module mimics a *very* small portion of FastAPI's surface needed by the
exercises.  It supports registering ``get`` and ``post`` routes and invoking
handlers synchronously through the accompanying :mod:`fastapi.testclient`
implementation.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional
import inspect


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

    def _handle_request(self, method: str, path: str, payload: Optional[Dict[str, Any]] = None):
        if method not in self._routes or path not in self._routes[method]:
            raise ValueError(f"No route registered for {method} {path}")

        route = self._routes[method][path]
        handler = route.handler
        payload = payload or {}

        bound_args = []
        kwargs: Dict[str, Any] = {}
        sig = inspect.signature(handler)

        for name, parameter in sig.parameters.items():
            annotation = parameter.annotation
            if annotation is inspect.Signature.empty:
                annotation = None

            if annotation is not None and hasattr(annotation, "model_validate"):
                argument = annotation.model_validate(payload)
            elif annotation is not None and hasattr(annotation, "__call__"):
                argument = annotation(**payload)
            else:
                argument = payload

            if parameter.kind in (
                inspect.Parameter.POSITIONAL_ONLY,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
            ):
                bound_args.append(argument)
            else:
                kwargs[name] = argument

        result = handler(*bound_args, **kwargs)
        return result


__all__ = ["FastAPI"]
