"""Placeholder R2 client for future signed THMC asset retrieval."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class R2Client:
    endpoint: str | None
    bucket: str | None
    access_key_present: bool = False
    secret_key_present: bool = False

    @property
    def available(self) -> bool:
        return bool(self.endpoint and self.bucket and self.access_key_present and self.secret_key_present)
