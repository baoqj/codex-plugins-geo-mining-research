"""Authentication helpers for optional live THMC integrations."""

from __future__ import annotations

from .config import masked_env_status


def get_auth_status() -> dict[str, bool]:
    """Return only boolean environment readiness; never expose secret values."""
    return masked_env_status()
