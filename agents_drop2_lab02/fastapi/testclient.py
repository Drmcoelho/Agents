"""Simplified ``fastapi.testclient`` compatible shim.

Only the behaviour required by the unit tests is implemented.  The test client
invokes the in-memory handlers registered by :class:`fastapi.FastAPI` and
returns lightweight response objects that mimic ``requests.Response`` enough
for ``response.status_code`` and ``response.json()`` usages.
"""

from __future__ import annotations

import inspect
from typing import Any, Dict, Iterable, Tuple

from . import FastAPI
from pydantic import BaseModel


class _Response:
    """Minimal response object returned by :class:`TestClient`."""

    def __init__(self, status_code: int, data: Any):
        self.status_code = status_code
        self._data = data

    def json(self) -> Any:
        return self._data


class TestClient:
    """Tiny subset of the real :class:`fastapi.testclient.TestClient`."""

    def __init__(self, app: FastAPI):
        self.app = app

    def get(self, path: str, **_: Any) -> _Response:
        handler = self._resolve("GET", path)
        if handler is None:
            return _Response(404, {"detail": "Not Found"})
        return self._execute(handler, ())

    def post(self, path: str, json: Dict[str, Any] | None = None, **_: Any) -> _Response:
        handler = self._resolve("POST", path)
        if handler is None:
            return _Response(404, {"detail": "Not Found"})
        json_payload = json or {}
        return self._execute(handler, (json_payload,))

    # --- Internal helpers -------------------------------------------------

    def _resolve(self, method: str, path: str):
        return self.app._routes.get((method.upper(), path))

    def _execute(self, handler, args: Iterable[Any]) -> _Response:
        parameters = list(inspect.signature(handler).parameters.values())
        call_args = []

        for provided_arg, parameter in zip(args, parameters):
            annotation = parameter.annotation
            if isinstance(annotation, type) and issubclass(annotation, BaseModel):
                call_args.append(annotation(**provided_arg))
            else:
                call_args.append(provided_arg)

        # If handler expects more parameters than payload provided (e.g. depends
        # injection) we simply fill with ``None`` to keep the stub predictable.
        if len(parameters) > len(call_args):
            call_args.extend([None] * (len(parameters) - len(call_args)))

        result = handler(*call_args)
        status_code = 200

        # Normalise the result into a JSON-serialisable representation.
        if isinstance(result, Tuple) and len(result) == 2 and isinstance(result[1], int):
            payload, status_code = result
        else:
            payload = result

        payload = _serialise(payload)
        return _Response(status_code, payload)


def _serialise(value: Any) -> Any:
    if isinstance(value, BaseModel):
        return value.dict()
    if isinstance(value, list):
        return [_serialise(item) for item in value]
    if isinstance(value, dict):
        return {key: _serialise(val) for key, val in value.items()}
    return value


__all__ = ["TestClient"]
