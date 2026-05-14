"""THMC run-record registry MCP tools."""

from __future__ import annotations

from typing import Any

from ..provenance import provenance
from ..schemas import tool_response
from ..storage import THMCStorage, get_default_storage


def save_thmc_run_record(
    project_id: str,
    model_id: str,
    model_version_id: str,
    solver: str,
    input_asset_ids: list[str] | None = None,
    output_asset_ids: list[str] | None = None,
    solver_version: str = "mock",
    parameters_hash: str | None = None,
    data_hash: str | None = None,
    status: str = "completed",
    warnings: list[str] | None = None,
    created_by: str = "geomine-thmc-mcp",
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = storage or get_default_storage()
    saved = store.save_run_record(
        {
            "project_id": project_id,
            "model_id": model_id,
            "model_version_id": model_version_id,
            "solver": solver,
            "solver_version": solver_version,
            "input_asset_ids": input_asset_ids or [],
            "output_asset_ids": output_asset_ids or [],
            "parameters_hash": parameters_hash,
            "data_hash": data_hash,
            "status": status,
            "warnings": warnings or ["mock run record"],
            "created_by": created_by,
        }
    )
    return tool_response(
        tool="save_thmc_run_record",
        query={"project_id": project_id, "model_id": model_id, "model_version_id": model_version_id, "solver": solver},
        mode="mock",
        results=[saved],
        provenance=provenance("THMC run registry", mode="mock", solver=solver, solver_version=solver_version),
        warnings=["Run record saved to local mock JSON registry; not synced to OpenMine live services."],
    )


def get_thmc_run_record(run_id: str, storage: THMCStorage | None = None) -> dict[str, Any]:
    store = storage or get_default_storage()
    run = store.get_run_record(run_id)
    query = {"run_id": run_id}
    if not run:
        return tool_response(
            tool="get_thmc_run_record",
            query=query,
            mode="error",
            ok=False,
            provenance=provenance("THMC run registry", mode="mock"),
            errors=[
                {
                    "code": "RUN_RECORD_NOT_FOUND",
                    "message": "Run record was not found in the local mock registry.",
                    "retryable": False,
                    "suggested_action": "Use list_thmc_run_records or save a run record first.",
                }
            ],
        )
    return tool_response(
        tool="get_thmc_run_record",
        query=query,
        mode="mock",
        results=[run],
        provenance=provenance("THMC run registry", mode="mock", solver=run.get("solver")),
    )


def list_thmc_run_records(
    project_id: str | None = None,
    model_id: str | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = storage or get_default_storage()
    return tool_response(
        tool="list_thmc_run_records",
        query={"project_id": project_id, "model_id": model_id},
        mode="mock",
        results=store.list_run_records(project_id=project_id, model_id=model_id),
        provenance=provenance("THMC run registry", mode="mock"),
    )
