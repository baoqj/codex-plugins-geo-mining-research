"""Typed schemas and response helpers for GeoMine THMC MCP tools."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Literal, NotRequired, TypedDict


Mode = Literal["live", "mock", "cached", "error"]


class ToolError(TypedDict):
    code: str
    message: str
    retryable: bool
    suggested_action: str


class ToolResponse(TypedDict):
    ok: bool
    mode: Mode
    tool: str
    query: dict[str, Any]
    results: list[dict[str, Any]]
    assets: list[dict[str, Any]]
    provenance: dict[str, Any]
    warnings: list[str]
    errors: list[ToolError]


class ProjectMetadata(TypedDict):
    project_id: str
    name: str
    jurisdiction: str
    commodity: list[str]
    stage: str
    updated_at: str


class AOI(TypedDict):
    aoi_id: str
    name: str
    crs: str
    bbox: dict[str, float]
    geometry_status: str


class WaterChemistrySample(TypedDict):
    sample_id: str
    location: dict[str, float]
    crs: str
    sample_date: str
    depth_interval: dict[str, float]
    field_parameters: dict[str, Any]
    lab_analytes: dict[str, dict[str, Any]]
    units: dict[str, str]
    detection_limits: dict[str, Any]
    qaqc_flags: list[str]
    source_file_id: str
    provenance: dict[str, Any]


class LithologyUnit(TypedDict):
    unit_id: str
    lithology: str
    geometry_status: str
    porosity: float
    permeability_m2: float
    fracture_density: str
    source: str
    confidence: str
    limitations: list[str]


class MineralAssemblage(TypedDict):
    unit_id: str
    minerals: list[dict[str, Any]]
    reactive_surface_area: NotRequired[str]
    source: str
    confidence: str
    limitations: list[str]


class MeshAsset(TypedDict):
    asset_id: str
    name: str
    asset_type: str
    format: str
    storage: str
    crs: str
    data_version: str
    checksum: str


class PHREEQCJob(TypedDict):
    job_id: str
    status: str
    run_mode: str
    database: str
    outputs: dict[str, Any]


class ComputeJob(TypedDict):
    job_id: str
    solver: str
    status: str
    model_version_id: str
    input_assets: dict[str, Any]


class THMCModelVersion(TypedDict):
    model_version_id: str
    project_id: str
    model_id: str
    version_label: str
    model_spec: dict[str, Any]
    source_asset_ids: list[str]
    notes: str
    saved_at: str


class THMCRunRecord(TypedDict):
    run_id: str
    project_id: str
    model_id: str
    model_version_id: str
    solver: str
    solver_version: str
    input_asset_ids: list[str]
    output_asset_ids: list[str]
    parameters_hash: str
    data_hash: str
    submitted_at: str
    completed_at: str | None
    status: str
    error_log: str | None
    warnings: list[str]
    created_by: str


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def tool_response(
    *,
    tool: str,
    query: dict[str, Any],
    mode: Mode = "mock",
    results: list[dict[str, Any]] | None = None,
    assets: list[dict[str, Any]] | None = None,
    provenance: dict[str, Any] | None = None,
    warnings: list[str] | None = None,
    errors: list[ToolError] | None = None,
    ok: bool = True,
) -> ToolResponse:
    return {
        "ok": ok,
        "mode": "error" if errors else mode,
        "tool": tool,
        "query": query,
        "results": results or [],
        "assets": assets or [],
        "provenance": {
            "retrieved_at": now_iso(),
            **(provenance or {}),
        },
        "warnings": warnings or [],
        "errors": errors or [],
    }


def unavailable_error(source: str, suggested_action: str) -> ToolError:
    return {
        "code": f"{source.upper()}_UNAVAILABLE",
        "message": f"{source} is not configured or unavailable.",
        "retryable": True,
        "suggested_action": suggested_action,
    }

