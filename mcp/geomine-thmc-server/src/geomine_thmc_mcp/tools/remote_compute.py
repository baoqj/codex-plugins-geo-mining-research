"""Mock job-based OGS/PFLOTRAN remote compute THMC MCP tools."""

from __future__ import annotations

from typing import Any

from ..adapters.ogs_project_builder import build_ogs_job_payload
from ..adapters.pflotran_input_builder import build_pflotran_job_payload
from ..provenance import provenance
from ..schemas import now_iso, tool_response
from ..storage import THMCStorage, get_default_storage


def _not_found(tool: str, query: dict[str, Any]) -> dict[str, Any]:
    return tool_response(
        tool=tool,
        query=query,
        mode="error",
        ok=False,
        provenance=provenance("THMC remote compute", mode="mock"),
        errors=[
            {
                "code": "COMPUTE_JOB_NOT_FOUND",
                "message": "Compute job was not found in the local mock job registry.",
                "retryable": False,
                "suggested_action": "Submit an OGS or PFLOTRAN job first, or check the job_id.",
            }
        ],
    )


def submit_ogs_job(
    project_id: str,
    model_version_id: str,
    mesh_asset_id: str,
    process_type: str = "ComponentTransport",
    parameters: dict[str, Any] | None = None,
    compute_profile: dict[str, Any] | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = storage or get_default_storage()
    payload, warnings = build_ogs_job_payload(
        project_id=project_id,
        model_version_id=model_version_id,
        mesh_asset_id=mesh_asset_id,
        process_type=process_type,
        parameters=parameters,
    )
    job = store.save_compute_job({**payload, "compute_profile": compute_profile or {"queue": "mock-local"}})
    return tool_response(
        tool="submit_ogs_job",
        query={
            "project_id": project_id,
            "model_version_id": model_version_id,
            "mesh_asset_id": mesh_asset_id,
            "process_type": process_type,
        },
        mode="mock",
        results=[job],
        provenance=provenance("THMC remote compute", mode="mock", solver="OGS", solver_version="mock"),
        warnings=warnings + ["Mock job submitted to local JSON registry; no OGS process was started."],
    )


def submit_pflotran_job(
    project_id: str,
    model_version_id: str,
    mesh_asset_id: str,
    chemistry_mode: str = "reactive_transport",
    parameters: dict[str, Any] | None = None,
    compute_profile: dict[str, Any] | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = storage or get_default_storage()
    payload, warnings = build_pflotran_job_payload(
        project_id=project_id,
        model_version_id=model_version_id,
        mesh_asset_id=mesh_asset_id,
        chemistry_mode=chemistry_mode,
        parameters=parameters,
    )
    job = store.save_compute_job({**payload, "compute_profile": compute_profile or {"queue": "mock-local"}})
    return tool_response(
        tool="submit_pflotran_job",
        query={
            "project_id": project_id,
            "model_version_id": model_version_id,
            "mesh_asset_id": mesh_asset_id,
            "chemistry_mode": chemistry_mode,
        },
        mode="mock",
        results=[job],
        provenance=provenance("THMC remote compute", mode="mock", solver="PFLOTRAN", solver_version="mock"),
        warnings=warnings + ["Mock job submitted to local JSON registry; no PFLOTRAN process was started."],
    )


def get_compute_job_status(job_id: str, storage: THMCStorage | None = None) -> dict[str, Any]:
    store = storage or get_default_storage()
    job = store.get_compute_job(job_id)
    query = {"job_id": job_id}
    if not job:
        return _not_found("get_compute_job_status", query)
    status = "running" if job.get("status") == "submitted" else job.get("status", "unknown")
    updated = store.update_compute_job(job_id, status=status, last_checked_at=now_iso()) or job
    return tool_response(
        tool="get_compute_job_status",
        query=query,
        mode="mock",
        results=[updated],
        provenance=provenance("THMC remote compute", mode="mock", solver=updated.get("solver")),
        warnings=["Mock job lifecycle: submitted jobs are advanced to running on first status check."],
    )


def fetch_compute_job_results(job_id: str, storage: THMCStorage | None = None) -> dict[str, Any]:
    store = storage or get_default_storage()
    job = store.get_compute_job(job_id)
    query = {"job_id": job_id}
    if not job:
        return _not_found("fetch_compute_job_results", query)
    completed = store.update_compute_job(job_id, status="completed", completed_at=now_iso()) or job
    output_asset = {
        "asset_id": f"{job_id}-results",
        "asset_type": "compute_results",
        "name": f"{job_id}-results.zip",
        "format": "zip",
        "storage": "mock-r2",
        "contents": ["summary.json", "mass_balance.csv", "state_0001.vtu", "run.log"],
        "created_at": now_iso(),
    }
    result = {
        **completed,
        "summary": {
            "mass_balance_status": "mock_not_evaluated",
            "convergence_status": "mock_completed",
            "scientific_interpretation": "not provided by MCP",
        },
    }
    return tool_response(
        tool="fetch_compute_job_results",
        query=query,
        mode="mock",
        results=[result],
        assets=[output_asset],
        provenance=provenance("THMC remote compute", mode="mock", solver=completed.get("solver")),
        warnings=["Mock result package; no numerical solver was executed."],
    )
