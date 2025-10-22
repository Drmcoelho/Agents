"""Minimal test client compatible with the simplified FastAPI stub."""
from __future__ import annotations

from typing import Any, Dict, Iterable, Mapping, Optional

from . import FastAPI
from pydantic import BaseModel


class Response:
    """Simple response container matching the subset used in the tests."""

    def __init__(self, status_code: int, json_data: Any):
        self.status_code = status_code
        self._json_data = json_data

    def json(self):
        return self._json_data


class TestClient:
    """Tiny synchronous test client mirroring the real FastAPI behaviour."""

    __test__ = False  # Prevent pytest from collecting this as a test case.

    def __init__(self, app: FastAPI):
        self.app = app

    def get(self, path: str):
        return self._build_response("GET", path, None)

    def post(self, path: str, json: Optional[Dict[str, Any]] = None):
        return self._build_response("POST", path, json or {})

    def _build_response(self, method: str, path: str, payload: Optional[Dict[str, Any]]):
        status_code, result = self.app._handle_request(method, path, payload)
        json_payload = self._serialize(result)
        return Response(status_code, json_payload)

    def _serialize(self, data: Any) -> Any:
        if isinstance(data, BaseModel):
            return data.model_dump()

        if isinstance(data, Mapping):
            return {key: self._serialize(value) for key, value in data.items()}

        if isinstance(data, Iterable) and not isinstance(data, (str, bytes)):
            return [self._serialize(item) for item in data]

        return data
