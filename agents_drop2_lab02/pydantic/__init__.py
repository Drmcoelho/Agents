"""Lightweight stub of :mod:`pydantic` for the educational labs.

Only the :class:`BaseModel` class with a tiny subset of its behaviour is
implemented.  The goal is to provide enough structure so type annotations and
``.dict()`` calls used inside the lab work without installing the real
dependency.
"""

from __future__ import annotations

from typing import Any


class BaseModel:
    """Very small stand-in for :class:`pydantic.BaseModel`."""

    def __init__(self, **data: Any):
        for key, value in data.items():
            setattr(self, key, value)

    def dict(self) -> dict[str, Any]:
        return dict(self.__dict__)

    # ``model_dump`` mirrors the modern Pydantic API and keeps parity with the
    # public surface in case student code prefers that spelling.
    def model_dump(self) -> dict[str, Any]:
        return self.dict()


__all__ = ["BaseModel"]
