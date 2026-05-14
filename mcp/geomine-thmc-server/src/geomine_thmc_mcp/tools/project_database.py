"""OpenMine project database THMC MCP tools."""

from __future__ import annotations

from typing import Any

from ..provenance import provenance
from ..schemas import tool_response
from ..storage import THMCStorage, get_default_storage


def _store(storage: THMCStorage | None) -> THMCStorage:
    return storage or get_default_storage()


def list_openmine_projects(
    status: str | None = "active",
    jurisdiction: str | None = None,
    commodity: str | None = None,
    limit: int = 20,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    query = {"status": status, "jurisdiction": jurisdiction, "commodity": commodity, "limit": limit}
    return tool_response(
        tool="list_openmine_projects",
        query=query,
        mode="mock",
        results=store.list_projects(status=status, jurisdiction=jurisdiction, commodity=commodity, limit=limit),
        provenance=provenance("OpenMine Project Database", mode="mock"),
        warnings=["Mock project database; do not treat as live OpenMine data."],
    )


def get_openmine_project(project_id: str, storage: THMCStorage | None = None) -> dict[str, Any]:
    store = _store(storage)
    project = store.get_project(project_id)
    if not project:
        return tool_response(
            tool="get_openmine_project",
            query={"project_id": project_id},
            mode="error",
            ok=False,
            provenance=provenance("OpenMine Project Database", mode="mock"),
            errors=[
                {
                    "code": "PROJECT_NOT_FOUND",
                    "message": f"Project not found in mock store: {project_id}",
                    "retryable": False,
                    "suggested_action": "Use list_openmine_projects to inspect available mock projects.",
                }
            ],
        )
    return tool_response(
        tool="get_openmine_project",
        query={"project_id": project_id},
        mode="mock",
        results=[project],
        provenance=provenance("OpenMine Project Database", mode="mock"),
        warnings=["Mock project metadata; live OpenMine database was not queried."],
    )


def get_project_aoi(
    project_id: str,
    aoi_id: str | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    aoi = store.get_aoi(project_id, aoi_id=aoi_id)
    if not aoi:
        return tool_response(
            tool="get_project_aoi",
            query={"project_id": project_id, "aoi_id": aoi_id},
            mode="error",
            ok=False,
            provenance=provenance("OpenMine Project Database", mode="mock"),
            errors=[
                {
                    "code": "AOI_NOT_FOUND",
                    "message": "Project AOI was not found in the mock store.",
                    "retryable": False,
                    "suggested_action": "Check project_id or aoi_id.",
                }
            ],
        )
    return tool_response(
        tool="get_project_aoi",
        query={"project_id": project_id, "aoi_id": aoi_id},
        mode="mock",
        results=[aoi],
        provenance=provenance("OpenMine Project Database", mode="mock", crs=aoi["crs"]),
        warnings=["Mock AOI only; not authoritative geometry."],
    )

