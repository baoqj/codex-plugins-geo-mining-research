"""Provenance helpers for THMC MCP tools."""

from __future__ import annotations

from typing import Any


def provenance(
    source: str,
    *,
    mode: str = "mock",
    data_version: str | None = "mock-2026-05-12",
    checksum: str | None = None,
    license: str | None = "internal mock data; not for interpretation",
    crs: str | None = None,
    units: str | dict[str, str] | None = None,
    **extra: Any,
) -> dict[str, Any]:
    data: dict[str, Any] = {
        "source": source,
        "mode": mode,
        "data_version": data_version,
        "license": license,
    }
    if checksum:
        data["checksum"] = checksum
    if crs:
        data["crs"] = crs
    if units:
        data["units"] = units
    data.update({key: value for key, value in extra.items() if value is not None})
    return data
