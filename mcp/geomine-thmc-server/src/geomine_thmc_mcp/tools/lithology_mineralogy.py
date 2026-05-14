"""Lithology and mineral assemblage THMC MCP tools."""

from __future__ import annotations

from typing import Any

from ..provenance import provenance
from ..schemas import tool_response
from ..storage import THMCStorage, get_default_storage


def query_lithology_units(
    project_id: str,
    aoi_id: str | None = None,
    include_geometry: bool = True,
    target_crs: str = "EPSG:4326",
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = storage or get_default_storage()
    query = {
        "project_id": project_id,
        "aoi_id": aoi_id,
        "include_geometry": include_geometry,
        "target_crs": target_crs,
    }
    return tool_response(
        tool="query_lithology_units",
        query=query,
        mode="mock",
        results=store.query_lithology(project_id, aoi_id=aoi_id),
        provenance=provenance("OpenMine Project Database / Lithology", mode="mock", crs=target_crs),
        warnings=["Mock lithology; not a site geological model."],
    )


def query_mineral_assemblages(
    project_id: str,
    unit_id: str | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = storage or get_default_storage()
    return tool_response(
        tool="query_mineral_assemblages",
        query={"project_id": project_id, "unit_id": unit_id},
        mode="mock",
        results=store.query_minerals(project_id, unit_id=unit_id),
        provenance=provenance("OpenMine Project Database / Mineral Assemblages", mode="mock"),
        warnings=["Mock mineral assemblage; XRD/QEMSCAN and reactive surface area measurements required for live modeling."],
    )

