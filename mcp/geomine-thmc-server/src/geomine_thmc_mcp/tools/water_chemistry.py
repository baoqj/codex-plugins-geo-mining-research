"""Water chemistry THMC MCP tools."""

from __future__ import annotations

from typing import Any

from ..provenance import provenance
from ..schemas import tool_response
from ..storage import THMCStorage, get_default_storage


def query_water_chemistry_samples(
    project_id: str,
    aoi_id: str | None = None,
    sample_types: list[str] | None = None,
    analytes: list[str] | None = None,
    date_range: dict[str, str] | None = None,
    include_qaqc: bool = True,
    limit: int = 5000,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = storage or get_default_storage()
    samples, warnings = store.query_water_samples(
        project_id=project_id,
        aoi_id=aoi_id,
        analytes=analytes,
        sample_types=sample_types,
        limit=limit,
    )
    query = {
        "project_id": project_id,
        "aoi_id": aoi_id,
        "sample_types": sample_types,
        "analytes": analytes,
        "date_range": date_range,
        "include_qaqc": include_qaqc,
        "limit": limit,
    }
    return tool_response(
        tool="query_water_chemistry_samples",
        query=query,
        mode="mock",
        results=samples,
        provenance=provenance(
            "OpenMine Project Database / Water Chemistry",
            mode="mock",
            units={"metals": "ug/L", "radionuclides": "Bq/L", "major_ions": "mg/L"},
        ),
        warnings=["Mock water chemistry; units and QA/QC flags are included for schema testing."] + warnings,
    )

