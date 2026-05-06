"""Mineral occurrence normalization helpers."""

from __future__ import annotations

from typing import Any


def _as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [part.strip() for part in value.split(",") if part.strip()]
    if isinstance(value, (list, tuple, set)):
        return [str(part).strip() for part in value if str(part).strip()]
    return [str(value)]


def normalize_occurrence(record: dict[str, Any]) -> dict[str, Any]:
    """Normalize common mineral occurrence fields while preserving source ids."""

    if not isinstance(record, dict):
        raise TypeError("record must be a dictionary")

    source_id = record.get("source_id") or record.get("id") or record.get("minfile_id") or record.get("omi_id")
    name = record.get("name") or record.get("occurrence_name") or record.get("property")
    source = record.get("source") or record.get("database") or "unknown"
    return {
        "source_id": source_id,
        "name": name,
        "source": source,
        "jurisdiction": record.get("jurisdiction") or record.get("province"),
        "commodities": _as_list(record.get("commodities") or record.get("commodity")),
        "deposit_model": record.get("deposit_model") or record.get("deposit_type"),
        "status": record.get("status"),
        "coordinates": record.get("coordinates") or record.get("geometry") or record.get("point"),
        "confidence_notes": record.get("confidence_notes")
        or record.get("location_confidence")
        or "No confidence notes supplied.",
        "original_record": dict(record),
    }
