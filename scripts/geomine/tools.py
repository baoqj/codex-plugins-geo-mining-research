"""Pure GeoMine MCP tool functions.

These functions do not import MCP. They are safe to unit test directly and are
wrapped by scripts/geomine_mcp_server.py.
"""

from __future__ import annotations

import os
from datetime import datetime, timezone
from typing import Any

from geomine.adapters import (
    ArcGisFeatureServiceAdapter,
    BcDataCatalogueAdapter,
    OpenCanadaCkanAdapter,
    get_source_registry,
)
from geomine.aoi import normalize_aoi


DEFAULT_USER_AGENT = "GeoMineResearch/0.2 (+https://openmine.vip)"
DEFAULT_MAX_ROWS = 25


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _network_default() -> bool:
    return os.environ.get("GEOMINE_ALLOW_NETWORK_DEFAULT", "false").lower() == "true"


def _max_rows() -> int:
    value = os.environ.get("GEOMINE_MAX_ROWS")
    if not value:
        return DEFAULT_MAX_ROWS
    try:
        parsed = int(value)
    except ValueError:
        return DEFAULT_MAX_ROWS
    return max(1, min(parsed, 100))


def _bounded_rows(rows: int, maximum: int | None = None) -> int:
    limit = maximum or _max_rows()
    if rows < 1:
        return 1
    return min(rows, limit)


def _base_result(
    data: dict[str, Any],
    provenance: dict[str, Any],
    warnings: list[str] | None = None,
    next_steps: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "data": data,
        "provenance": {
            "tool_layer": "scripts/geomine/tools.py",
            "retrieved_at": _now_iso(),
            **provenance,
        },
        "warnings": warnings or [],
        "next_steps": next_steps or [],
    }


def _adapter_info(adapter: Any) -> dict[str, str | None]:
    return {
        "name": getattr(adapter, "name", adapter.__class__.__name__),
        "version": getattr(adapter, "version", None),
    }


def _normalize_jurisdiction(value: str | None) -> str:
    return (value or "").strip().lower()


def _planned_request(adapter: Any, url: str, query: dict[str, Any], source: str | None = None) -> dict[str, Any]:
    return {
        "adapter": _adapter_info(adapter),
        "source": source,
        "source_note": adapter.source_note() if hasattr(adapter, "source_note") else None,
        "url": url,
        "query": query,
        "retrieval_status": "planned",
    }


def _bbox_geometry(bbox: dict[str, float] | None) -> tuple[dict[str, Any] | None, str | None]:
    if not bbox:
        return None, None
    required = {"xmin", "ymin", "xmax", "ymax"}
    missing = sorted(required - set(bbox))
    if missing:
        return None, f"bbox is missing required keys: {', '.join(missing)}."
    return (
        {
            "xmin": bbox["xmin"],
            "ymin": bbox["ymin"],
            "xmax": bbox["xmax"],
            "ymax": bbox["ymax"],
            "spatialReference": {"wkid": 4326},
        },
        None,
    )


def resolve_aoi_tool(input_data: dict[str, Any]) -> dict[str, Any]:
    aoi = normalize_aoi(input_data)
    return _base_result(
        data=aoi.as_dict(),
        provenance={
            "source": "local-normalizer",
            "retrieval_status": "parsed",
            "network": "not-used",
            "query_parameters": {"input_keys": sorted(input_data.keys())},
        },
        warnings=list(aoi.warnings),
        next_steps=[
            "Confirm authoritative AOI geometry before calculating distance, area, buffer, or occurrence proximity.",
            "Confirm CRS before integrating GIS layers.",
        ],
    )


def search_geodata_sources_tool(
    query: str,
    jurisdiction: str | None = None,
    data_type: str | None = None,
    rows: int = 10,
    allow_network: bool = False,
) -> dict[str, Any]:
    rows = _bounded_rows(rows)
    allow_network = bool(allow_network or _network_default())

    adapters: list[OpenCanadaCkanAdapter | BcDataCatalogueAdapter] = [OpenCanadaCkanAdapter()]
    jurisdiction_key = _normalize_jurisdiction(jurisdiction)
    if jurisdiction_key in {"bc", "b.c.", "british columbia"}:
        adapters.append(BcDataCatalogueAdapter())

    query_parameters = {
        "q": query,
        "jurisdiction": jurisdiction,
        "data_type": data_type,
        "rows": rows,
        "allow_network": allow_network,
    }
    planned_requests = [
        _planned_request(
            adapter=adapter,
            source=adapter.source_name,
            url=adapter.build_package_search_url(query=query, rows=rows),
            query=query_parameters,
        )
        for adapter in adapters
    ]

    if not allow_network:
        return _base_result(
            data={
                "planned_requests": planned_requests,
                "registry": get_source_registry(),
                "results": [],
            },
            provenance={
                "retrieval_status": "planned",
                "network": "disabled",
                "adapters": [_adapter_info(adapter) for adapter in adapters],
                "query_parameters": query_parameters,
            },
            warnings=[
                "Network disabled; no live catalogue records were fetched.",
                "Catalogue discovery is not source validation; each linked resource requires separate verification.",
            ],
            next_steps=[
                "Run again with allow_network=true only after query scope is confirmed.",
                "Filter resources by format, license, date, CRS, and provider before interpretation.",
            ],
        )

    return _base_result(
        data={
            "planned_requests": planned_requests,
            "results": [],
        },
        provenance={
            "retrieval_status": "unsupported",
            "network": "requested-but-not-implemented",
            "adapters": [_adapter_info(adapter) for adapter in adapters],
            "query_parameters": query_parameters,
            "user_agent": os.environ.get("GEOMINE_USER_AGENT", DEFAULT_USER_AGENT),
        },
        warnings=[
            "allow_network=true was requested, but live HTTP retrieval is not implemented in this version.",
        ],
        next_steps=[
            "Implement bounded httpx retrieval with timeout, user agent, cache, and fixture-backed parser tests.",
        ],
    )


def search_mineral_occurrences_tool(
    jurisdiction: str,
    commodity: str | None = None,
    deposit_model: str | None = None,
    bbox: dict[str, float] | None = None,
    rows: int = 10,
    allow_network: bool = False,
) -> dict[str, Any]:
    rows = _bounded_rows(rows)
    allow_network = bool(allow_network or _network_default())
    jurisdiction_key = _normalize_jurisdiction(jurisdiction)
    query_parameters = {
        "jurisdiction": jurisdiction,
        "commodity": commodity,
        "deposit_model": deposit_model,
        "bbox": bbox,
        "rows": rows,
        "allow_network": allow_network,
    }

    planned_requests: list[dict[str, Any]] = []
    adapters: list[dict[str, str | None]] = []
    warnings = [
        "No occurrence proximity or target ranking was calculated.",
        "Location confidence, source CRS, and occurrence identifiers must be verified before interpretation.",
    ]

    if jurisdiction_key in {"bc", "b.c.", "british columbia"}:
        bc = BcDataCatalogueAdapter()
        adapters.append(_adapter_info(bc))
        planned_requests.append(
            _planned_request(
                adapter=bc,
                source="BC Data Catalogue / MINFILE",
                url=bc.build_package_search_url(query="MINFILE mineral occurrence", rows=rows),
                query={**query_parameters, "q": "MINFILE mineral occurrence"},
            )
        )

    if jurisdiction_key in {"ontario", "on"}:
        planned_requests.append(
            {
                "adapter": {
                    "name": "ontario-ogsearth-roadmap",
                    "version": None,
                },
                "source": "Ontario OGSEarth / Ontario Mineral Inventory",
                "url": "https://www.geologyontario.mndm.gov.on.ca/ogsearth.html",
                "query": query_parameters,
                "retrieval_status": "roadmap-only",
            }
        )

    geometry, bbox_warning = _bbox_geometry(bbox)
    if bbox_warning:
        warnings.append(bbox_warning)
    if geometry:
        usgs = ArcGisFeatureServiceAdapter(
            service_url="https://energy.usgs.gov/arcgis/rest/services/MRData/Mineral_Resource_Data_System/MapServer",
            source_name="USGS MRData",
            jurisdiction="United States and global extension",
        )
        adapters.append(_adapter_info(usgs))
        planned_requests.append(
            _planned_request(
                adapter=usgs,
                source="USGS MRData ArcGIS REST",
                url=usgs.build_query_url(geometry=geometry, result_record_count=rows),
                query=query_parameters,
            )
        )

    if not planned_requests:
        warnings.append("No source-specific occurrence adapter is available for the requested jurisdiction in this version.")

    return _base_result(
        data={
            "planned_requests": planned_requests,
            "occurrences": [],
            "query": query_parameters,
        },
        provenance={
            "retrieval_status": "planned" if not allow_network else "unsupported",
            "network": "disabled" if not allow_network else "requested-but-not-implemented",
            "adapters": adapters,
            "query_parameters": query_parameters,
        },
        warnings=warnings
        + (
            ["allow_network=true was requested, but live mineral occurrence retrieval is not implemented in this version."]
            if allow_network
            else []
        ),
        next_steps=[
            "Normalize MINFILE / OMI / MRData identifiers after live retrieval is implemented.",
            "Use confirmed AOI geometry and CRS before calculating distances.",
        ],
    )


def fetch_geochem_metadata_tool(
    source: str | None = None,
    survey_id: str | None = None,
    source_url: str | None = None,
    jurisdiction: str | None = None,
    allow_network: bool = False,
) -> dict[str, Any]:
    allow_network = bool(allow_network or _network_default())
    query_parameters = {
        "source": source,
        "survey_id": survey_id,
        "source_url": source_url,
        "jurisdiction": jurisdiction,
        "allow_network": allow_network,
    }
    candidate_keys = {"nrcan-cdogs", "usgs-mrdata-arcgis", "ontario-ogsearth"}
    candidate_sources = [item for item in get_source_registry() if item["key"] in candidate_keys]

    return _base_result(
        data={
            "metadata": [],
            "query": query_parameters,
            "candidate_sources": candidate_sources,
        },
        provenance={
            "retrieval_status": "planned" if not allow_network else "unsupported",
            "network": "disabled" if not allow_network else "requested-but-not-implemented",
            "query_parameters": query_parameters,
        },
        warnings=[
            "No live geochemical metadata was fetched.",
            "Analytical spreadsheets are not parsed in this MCP version.",
            "Sample medium, analytical method, detection limits, units, and QA/QC status remain unverified.",
        ]
        + (
            ["allow_network=true was requested, but live geochemical metadata retrieval is not implemented in this version."]
            if allow_network
            else []
        ),
        next_steps=[
            "Implement CDoGS metadata fixture parser before live retrieval.",
            "Do not compare geochemical surveys until medium, method, units, and detection limits are normalized.",
        ],
    )


def retrieve_assessment_reports_tool(
    jurisdiction: str,
    project_name: str | None = None,
    report_id: str | None = None,
    nts_sheet: str | None = None,
    commodity: str | None = None,
    allow_network: bool = False,
) -> dict[str, Any]:
    allow_network = bool(allow_network or _network_default())
    query_parameters = {
        "jurisdiction": jurisdiction,
        "project_name": project_name,
        "report_id": report_id,
        "nts_sheet": nts_sheet,
        "commodity": commodity,
        "allow_network": allow_network,
    }

    return _base_result(
        data={
            "planned_sources": [
                {
                    "source": "BC ARIS / Property File",
                    "jurisdiction": "British Columbia",
                    "retrieval_status": "planned",
                },
                {
                    "source": "Ontario Assessment File Database",
                    "jurisdiction": "Ontario",
                    "retrieval_status": "planned",
                },
            ],
            "query": query_parameters,
            "reports": [],
        },
        provenance={
            "retrieval_status": "planned" if not allow_network else "unsupported",
            "network": "disabled" if not allow_network else "requested-but-not-implemented",
            "query_parameters": query_parameters,
        },
        warnings=[
            "No assessment report metadata was fetched.",
            "No PDF files were downloaded.",
            "Historical assessment reports may contain outdated coordinates, methods, or resource terminology.",
        ]
        + (
            ["allow_network=true was requested, but live assessment report retrieval is not implemented in this version."]
            if allow_network
            else []
        ),
        next_steps=[
            "Implement jurisdiction-specific report metadata adapters before downloading files.",
            "Preserve report id, author, year, title, source URL, and access notes.",
        ],
    )
