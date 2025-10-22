"""Minimal FastAPI-compatible stubs used for the educational lab.

This project intentionally avoids external dependencies, but the lab
implementation imports :mod:`fastapi`.  To keep the exercises focused on the
Model Context Protocol instead of framework setup, we provide a very small
subset of the FastAPI surface that is sufficient for the unit tests.  Only the
behaviour required by ``labs/02_mcp/py/server.py`` is implemented: declaring
``GET`` and ``POST`` routes and invoking them via the accompanying
``TestClient``.

The goal of this shim is not to be feature complete—just ergonomic enough so
the rest of the lab code reads naturally.  Students can later swap this module
for the real dependency without changing the server logic.
"""

from __future__ import annotations

from typing import Any, Callable, Dict, Tuple


RouteHandler = Callable[..., Any]


class FastAPI:
    """Very small subset of the :class:`fastapi.FastAPI` interface.

    Only the functionality exercised by the tests is included: route
    registration through ``@app.get`` and ``@app.post`` decorators.  The
    returned callable is stored and later exercised by the simplified test
    client.
    """

    def __init__(self, title: str | None = None, description: str | None = None):
        self.title = title
        self.description = description
        self._routes: Dict[Tuple[str, str], RouteHandler] = {}

    def _register(self, method: str, path: str, func: RouteHandler) -> RouteHandler:
        self._routes[(method.upper(), path)] = func
        return func

    def get(self, path: str, **_: Any) -> Callable[[RouteHandler], RouteHandler]:
        """Decorator used to register a ``GET`` handler."""

        def decorator(func: RouteHandler) -> RouteHandler:
            return self._register("GET", path, func)

        return decorator

    def post(self, path: str, **_: Any) -> Callable[[RouteHandler], RouteHandler]:
        """Decorator used to register a ``POST`` handler."""

        def decorator(func: RouteHandler) -> RouteHandler:
            return self._register("POST", path, func)

        return decorator


__all__ = ["FastAPI"]
