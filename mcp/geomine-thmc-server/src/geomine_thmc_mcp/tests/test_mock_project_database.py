from __future__ import annotations

from geomine_thmc_mcp.storage import THMCStorage
from geomine_thmc_mcp.tools import get_openmine_project, list_openmine_projects, query_water_chemistry_samples


def test_mock_project_database_contains_uranium_groundwater_project(tmp_path):
    storage = THMCStorage(cache_dir=tmp_path, mode="mock")
    projects = list_openmine_projects(commodity="uranium", storage=storage)
    assert projects["results"][0]["project_id"] == "om-prj-uranium-001"
    project = get_openmine_project("om-prj-uranium-001", storage=storage)
    assert "radionuclide" in project["results"][0]["research_objective"]


def test_water_chemistry_mock_exposes_units_and_qaqc(tmp_path):
    storage = THMCStorage(cache_dir=tmp_path, mode="mock")
    response = query_water_chemistry_samples("om-prj-uranium-001", analytes=["U", "Ra226"], storage=storage)
    assert response["results"]
    assert response["results"][0]["units"]["radionuclides"] == "Bq/L"
    assert "qaqc_flags" in response["results"][0]
