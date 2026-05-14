from __future__ import annotations

from geomine_thmc_mcp.storage import THMCStorage
from geomine_thmc_mcp.tools import build_phreeqc_input, run_phreeqc_job


def test_build_phreeqc_input_contains_solution_and_selected_output(tmp_path):
    storage = THMCStorage(cache_dir=tmp_path, mode="mock")
    response = build_phreeqc_input("om-prj-uranium-001", "model-001", storage=storage)
    content = response["assets"][0]["content"]
    assert "SOLUTION 1 GW-001" in content
    assert "SELECTED_OUTPUT 1" in content
    assert response["warnings"]


def test_run_phreeqc_job_returns_mock_selected_output(tmp_path):
    storage = THMCStorage(cache_dir=tmp_path, mode="mock")
    response = run_phreeqc_job("om-prj-uranium-001", "model-001", storage=storage)
    assert response["results"][0]["status"] == "completed"
    assert response["assets"][0]["asset_type"] == "phreeqc_selected_output"
    assert "Mock PHREEQC execution" in response["warnings"][0]
