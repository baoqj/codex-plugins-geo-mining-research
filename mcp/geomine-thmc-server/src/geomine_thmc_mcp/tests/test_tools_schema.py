from __future__ import annotations

from geomine_thmc_mcp.storage import THMCStorage
from geomine_thmc_mcp.tools import (
    build_phreeqc_input,
    fetch_mesh_or_parameter_field,
    get_openmine_project,
    get_project_aoi,
    get_thmc_mesh_catalog,
    list_openmine_projects,
    query_lithology_units,
    query_mineral_assemblages,
    query_water_chemistry_samples,
    run_phreeqc_job,
)


PROJECT_ID = "om-prj-uranium-001"
REQUIRED_KEYS = {"ok", "mode", "tool", "query", "results", "assets", "provenance", "warnings", "errors"}


def assert_response(payload: dict, tool: str) -> None:
    assert REQUIRED_KEYS.issubset(payload)
    assert payload["ok"] is True
    assert payload["mode"] == "mock"
    assert payload["tool"] == tool


def test_primary_data_tools_return_unified_schema(tmp_path):
    storage = THMCStorage(cache_dir=tmp_path, mode="mock")
    calls = [
        ("list_openmine_projects", list_openmine_projects(storage=storage)),
        ("get_openmine_project", get_openmine_project(PROJECT_ID, storage=storage)),
        ("get_project_aoi", get_project_aoi(PROJECT_ID, storage=storage)),
        ("query_water_chemistry_samples", query_water_chemistry_samples(PROJECT_ID, storage=storage)),
        ("query_lithology_units", query_lithology_units(PROJECT_ID, storage=storage)),
        ("query_mineral_assemblages", query_mineral_assemblages(PROJECT_ID, storage=storage)),
        ("get_thmc_mesh_catalog", get_thmc_mesh_catalog(PROJECT_ID, storage=storage)),
        ("fetch_mesh_or_parameter_field", fetch_mesh_or_parameter_field(PROJECT_ID, "mesh", storage=storage)),
        ("build_phreeqc_input", build_phreeqc_input(PROJECT_ID, "model-001", storage=storage)),
        ("run_phreeqc_job", run_phreeqc_job(PROJECT_ID, "model-001", storage=storage)),
    ]
    for tool, response in calls:
        assert_response(response, tool)
