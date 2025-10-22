"""Tiny subset of Pydantic's :mod:`BaseModel` sufficient for the lab tests."""
from __future__ import annotations

from typing import Any, Dict


class BaseModel:
    def __init__(self, **data: Any):
        for key, value in data.items():
            setattr(self, key, value)

    @classmethod
    def model_validate(cls, data: Dict[str, Any] | "BaseModel") -> "BaseModel":
        if isinstance(data, cls):
            return data
        return cls(**data)

    def dict(self) -> Dict[str, Any]:
        return self.__dict__.copy()


__all__ = ["BaseModel"]
