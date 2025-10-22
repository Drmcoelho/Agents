"""Minimal test client compatible with the simplified FastAPI stub."""
from __future__ import annotations

from typing import Any, Dict, Optional

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
        result = self.app._handle_request(method, path, payload)

        if isinstance(result, BaseModel):
            json_payload = result.model_dump()
        else:
            json_payload = result

        return Response(200, json_payload)
