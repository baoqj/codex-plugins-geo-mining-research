"""OpenGeoSys job payload builder for GeoMine THMC MCP."""

from __future__ import annotations

from typing import Any


def build_ogs_job_payload(
    *,
    project_id: str,
    model_version_id: str,
    mesh_asset_id: str,
    process_type: str = "ComponentTransport",
    parameters: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], list[str]]:
    warnings = [
        "OGS payload is a job-submission scaffold; validate mesh quality, boundary conditions, units, and chemistry coupling before production runs.",
    ]
    payload = {
        "solver": "OGS",
        "project_id": project_id,
        "model_version_id": model_version_id,
        "input_assets": {
            "mesh_asset_id": mesh_asset_id,
            "project_file": f"{model_version_id}.prj",
        },
        "process_type": process_type,
        "parameters": parameters or {},
    }
    return payload, warnings
