"""PFLOTRAN job payload builder for GeoMine THMC MCP."""

from __future__ import annotations

from typing import Any


def build_pflotran_job_payload(
    *,
    project_id: str,
    model_version_id: str,
    mesh_asset_id: str,
    chemistry_mode: str = "reactive_transport",
    parameters: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], list[str]]:
    warnings = [
        "PFLOTRAN payload is a job-submission scaffold; validate grid conversion, reaction database, timestep controls, and HPC resource settings before production runs.",
    ]
    payload = {
        "solver": "PFLOTRAN",
        "project_id": project_id,
        "model_version_id": model_version_id,
        "input_assets": {
            "mesh_asset_id": mesh_asset_id,
            "input_file": f"{model_version_id}.in",
        },
        "chemistry_mode": chemistry_mode,
        "parameters": parameters or {},
    }
    return payload, warnings
