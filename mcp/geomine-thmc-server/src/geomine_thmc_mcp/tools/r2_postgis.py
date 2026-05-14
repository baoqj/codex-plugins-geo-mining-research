"""R2/PostGIS-like mesh and parameter field THMC MCP tools."""

from __future__ import annotations

from typing import Any

from ..provenance import provenance
from ..schemas import tool_response
from ..storage import THMCStorage, get_default_storage


def get_thmc_mesh_catalog(project_id: str, storage: THMCStorage | None = None) -> dict[str, Any]:
    store = storage or get_default_storage()
    assets = store.list_assets(project_id, asset_type=None)
    mesh_assets = [asset for asset in assets if asset["asset_type"] == "mesh"]
    field_assets = [asset for asset in assets if asset["asset_type"] == "parameter_field"]
    return tool_response(
        tool="get_thmc_mesh_catalog",
        query={"project_id": project_id},
        mode="mock",
        results=mesh_assets,
        assets=field_assets,
        provenance=provenance("R2/PostGIS THMC asset catalog", mode="mock", crs="EPSG:32613"),
        warnings=["Mock asset catalog; signed URLs are intentionally omitted."],
    )


def fetch_mesh_or_parameter_field(
    project_id: str,
    asset_type: str,
    field_name: str | None = None,
    format: str | None = None,
    target_crs: str | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = storage or get_default_storage()
    asset = store.get_asset(project_id, asset_type=asset_type, field_name=field_name)
    query = {
        "project_id": project_id,
        "asset_type": asset_type,
        "field_name": field_name,
        "format": format,
        "target_crs": target_crs,
    }
    if not asset:
        return tool_response(
            tool="fetch_mesh_or_parameter_field",
            query=query,
            mode="error",
            ok=False,
            provenance=provenance("R2/PostGIS THMC asset catalog", mode="mock"),
            errors=[
                {
                    "code": "ASSET_NOT_FOUND",
                    "message": "Requested mesh or parameter field was not found in mock asset catalog.",
                    "retryable": False,
                    "suggested_action": "Use get_thmc_mesh_catalog to inspect available assets.",
                }
            ],
        )
    return tool_response(
        tool="fetch_mesh_or_parameter_field",
        query=query,
        mode="mock",
        assets=[asset],
        provenance=provenance(
            "R2/PostGIS THMC asset catalog",
            mode="mock",
            data_version=asset["data_version"],
            checksum=asset["checksum"],
            crs=target_crs or asset["crs"],
        ),
        warnings=["Mock asset metadata only; no signed URL is returned to avoid leaking sensitive links."],
    )

