"""THMC model-version registry MCP tools."""

from __future__ import annotations

from typing import Any

from ..provenance import provenance
from ..schemas import tool_response
from ..storage import THMCStorage, get_default_storage


def save_thmc_model_version(
    project_id: str,
    model_id: str,
    version_label: str,
    model_spec: dict[str, Any],
    source_asset_ids: list[str] | None = None,
    notes: str = "",
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = storage or get_default_storage()
    saved = store.save_model_version(
        {
            "project_id": project_id,
            "model_id": model_id,
            "version_label": version_label,
            "model_spec": model_spec,
            "source_asset_ids": source_asset_ids or [],
            "notes": notes,
        }
    )
    return tool_response(
        tool="save_thmc_model_version",
        query={"project_id": project_id, "model_id": model_id, "version_label": version_label},
        mode="mock",
        results=[saved],
        provenance=provenance("THMC model registry", mode="mock"),
        warnings=["Model version saved to local mock JSON registry; not synced to OpenMine live services."],
    )


def get_thmc_model_version(model_version_id: str, storage: THMCStorage | None = None) -> dict[str, Any]:
    store = storage or get_default_storage()
    version = store.get_model_version(model_version_id)
    query = {"model_version_id": model_version_id}
    if not version:
        return tool_response(
            tool="get_thmc_model_version",
            query=query,
            mode="error",
            ok=False,
            provenance=provenance("THMC model registry", mode="mock"),
            errors=[
                {
                    "code": "MODEL_VERSION_NOT_FOUND",
                    "message": "Model version was not found in the local mock registry.",
                    "retryable": False,
                    "suggested_action": "Use list_thmc_model_versions or save a model version first.",
                }
            ],
        )
    return tool_response(
        tool="get_thmc_model_version",
        query=query,
        mode="mock",
        results=[version],
        provenance=provenance("THMC model registry", mode="mock"),
    )


def list_thmc_model_versions(
    project_id: str | None = None,
    model_id: str | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = storage or get_default_storage()
    return tool_response(
        tool="list_thmc_model_versions",
        query={"project_id": project_id, "model_id": model_id},
        mode="mock",
        results=store.list_model_versions(project_id=project_id, model_id=model_id),
        provenance=provenance("THMC model registry", mode="mock"),
    )
