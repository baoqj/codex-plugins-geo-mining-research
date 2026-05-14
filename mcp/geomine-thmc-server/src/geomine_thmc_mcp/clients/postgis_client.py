"""Placeholder PostGIS client for future live geometry and parameter-field reads."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PostGISClient:
    dsn_present: bool = False

    @property
    def available(self) -> bool:
        return self.dsn_present
