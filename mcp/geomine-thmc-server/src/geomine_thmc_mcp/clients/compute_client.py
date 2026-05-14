"""Placeholder remote compute client for future OGS/PFLOTRAN service integration."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ComputeClient:
    api_url: str | None
    token_present: bool = False

    @property
    def available(self) -> bool:
        return bool(self.api_url and self.token_present)
