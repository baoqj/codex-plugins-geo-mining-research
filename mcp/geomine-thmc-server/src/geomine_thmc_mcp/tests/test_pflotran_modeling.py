from __future__ import annotations

from geomine_thmc_mcp.storage import THMCStorage
from geomine_thmc_mcp.tools import (
    build_pflotran_input_deck,
    build_pflotran_result_summary,
    build_pflotran_run_manifest,
    get_pflotran_model_package,
    list_pflotran_model_packages,
    parse_pflotran_observation_output,
    save_pflotran_model_package,
    validate_pflotran_input_deck,
)


PROJECT_ID = "om-prj-uranium-001"
REQUIRED_KEYS = {"ok", "mode", "tool", "query", "results", "assets", "provenance", "warnings", "errors"}


def assert_response(payload: dict, tool: str) -> None:
    assert REQUIRED_KEYS.issubset(payload)
    assert payload["ok"] is True
    assert payload["mode"] == "mock"
    assert payload["tool"] == tool


def test_pflotran_planning_tools(tmp_path):
    storage = THMCStorage(cache_dir=tmp_path, mode="mock")
    deck = build_pflotran_input_deck(PROJECT_ID, "pflotran-model-001")
    assert_response(deck, "build_pflotran_input_deck")
    input_deck = deck["results"][0]["input_deck"]
    validation = validate_pflotran_input_deck(input_deck)
    assert_response(validation, "validate_pflotran_input_deck")
    manifest = build_pflotran_run_manifest("pflotran-model-001", mpi_processes=8)
    assert_response(manifest, "build_pflotran_run_manifest")
    parsed = parse_pflotran_observation_output("time,pH,U\n0,7.2,0.01\n1,7.1,0.02\n")
    assert_response(parsed, "parse_pflotran_observation_output")
    summary = build_pflotran_result_summary(parsed["results"][0]["rows"])
    assert_response(summary, "build_pflotran_result_summary")
    saved = save_pflotran_model_package(
        PROJECT_ID,
        "test-package",
        {"scenario": "uranium_reactive_transport"},
        storage=storage,
    )
    assert_response(saved, "save_pflotran_model_package")
    package_id = saved["results"][0]["package_id"]
    assert_response(get_pflotran_model_package(package_id, storage=storage), "get_pflotran_model_package")
    listed = list_pflotran_model_packages(PROJECT_ID, storage=storage)
    assert_response(listed, "list_pflotran_model_packages")
    assert listed["results"][0]["package_id"] == package_id
