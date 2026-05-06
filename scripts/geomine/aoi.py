"""AOI normalization without external geocoding."""

from __future__ import annotations

from typing import Any

from .evidence_schema import NormalizedAOI


def _first_present(input_data: dict[str, Any], *keys: str) -> Any | None:
    for key in keys:
        if key in input_data and input_data[key] not in (None, ""):
            return input_data[key]
    return None


def normalize_aoi(input_data: dict[str, Any]) -> NormalizedAOI:
    """Normalize simple AOI dictionaries into a shared record.

    This helper intentionally does not geocode property names, resolve claim
    boundaries, or reproject coordinates.
    """

    if not isinstance(input_data, dict):
        raise TypeError("input_data must be a dictionary")

    name = _first_present(input_data, "name", "property", "project", "claim_block")
    province = _first_present(input_data, "province_or_territory", "province", "territory")
    country = _first_present(input_data, "country") or "Canada"
    coordinates = _first_present(input_data, "coordinates", "polygon", "bbox", "point")
    crs = _first_present(input_data, "crs", "input_crs")
    nts_sheet = _first_present(input_data, "nts_sheet", "nts")

    assumptions: list[str] = []
    warnings: list[str] = []

    if country == "Canada" and not province:
        warnings.append("Canadian AOI is missing province or territory.")
    if not crs:
        assumptions.append("No CRS supplied; treat coordinates as unresolved until confirmed.")
        warnings.append("CRS missing; do not calculate distance, area, or buffers.")
    if not coordinates:
        warnings.append("No coordinates, polygon, bounding box, or point supplied.")
    if name and not coordinates:
        assumptions.append("Property or project name was preserved, but no geocoding was attempted.")
    if nts_sheet and not province:
        assumptions.append("NTS sheet can help identify jurisdiction but was not resolved automatically.")

    return NormalizedAOI(
        name=str(name) if name else None,
        province_or_territory=str(province) if province else None,
        country=str(country),
        coordinates=coordinates,
        crs=str(crs) if crs else None,
        nts_sheet=str(nts_sheet) if nts_sheet else None,
        assumptions=assumptions,
        warnings=warnings,
    )
