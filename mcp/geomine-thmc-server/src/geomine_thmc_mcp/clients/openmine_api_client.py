"""Placeholder OpenMine API client for future live mode."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OpenMineAPIClient:
    base_url: str | None
    token_present: bool = False

    @property
    def available(self) -> bool:
        return bool(self.base_url and self.token_present)
