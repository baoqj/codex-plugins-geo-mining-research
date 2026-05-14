#!/usr/bin/env python3
"""Run direct GeoMine THMC MCP tool smoke checks without starting an MCP client."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THMC_SRC = ROOT / "mcp" / "geomine-thmc-server" / "src"
sys.path.insert(0, str(THMC_SRC))

from geomine_thmc_mcp.storage import THMCStorage  # noqa: E402
from geomine_thmc_mcp.tools import (  # noqa: E402
    build_phreeqc_input,
    fetch_compute_job_results,
    fetch_mesh_or_parameter_field,
    get_compute_job_status,
    get_openmine_project,
    get_project_aoi,
    get_thmc_mesh_catalog,
    get_thmc_model_version,
    get_thmc_run_record,
    list_openmine_projects,
    list_thmc_model_versions,
    list_thmc_run_records,
    query_lithology_units,
    query_mineral_assemblages,
    query_water_chemistry_samples,
    run_phreeqc_job,
    save_thmc_model_version,
    save_thmc_run_record,
    submit_ogs_job,
    submit_pflotran_job,
)


PROJECT_ID = "om-prj-uranium-001"


def assert_response(payload: dict, expected_tool: str) -> None:
    required = {"ok", "mode", "tool", "query", "results", "assets", "provenance", "warnings", "errors"}
    missing = required.difference(payload)
    if missing:
        raise AssertionError(f"{expected_tool} missing keys: {sorted(missing)}")
    if payload["tool"] != expected_tool:
        raise AssertionError(f"{expected_tool} reported tool={payload['tool']}")
    if payload["mode"] not in {"mock", "live", "cached", "error"}:
        raise AssertionError(f"{expected_tool} invalid mode={payload['mode']}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="geomine-thmc-") as tmp:
        storage = THMCStorage(cache_dir=Path(tmp), mode="mock")
        responses: list[dict] = []
        responses.append(list_openmine_projects(storage=storage))
        responses.append(get_openmine_project(PROJECT_ID, storage=storage))
        responses.append(get_project_aoi(PROJECT_ID, storage=storage))
        responses.append(query_water_chemistry_samples(PROJECT_ID, storage=storage))
        responses.append(query_lithology_units(PROJECT_ID, storage=storage))
        responses.append(query_mineral_assemblages(PROJECT_ID, storage=storage))
        responses.append(get_thmc_mesh_catalog(PROJECT_ID, storage=storage))
        responses.append(fetch_mesh_or_parameter_field(PROJECT_ID, "mesh", storage=storage))
        responses.append(build_phreeqc_input(PROJECT_ID, "model-001", storage=storage))
        responses.append(run_phreeqc_job(PROJECT_ID, "model-001", storage=storage))

        model = save_thmc_model_version(
            PROJECT_ID,
            "model-001",
            "v0.1-mock",
            {"scenario": "uranium_mine_groundwater", "coupling_level": "THC"},
            source_asset_ids=["mesh-2d-cross-section-001"],
            storage=storage,
        )
        model_version_id = model["results"][0]["model_version_id"]
        responses.append(model)
        responses.append(get_thmc_model_version(model_version_id, storage=storage))
        responses.append(list_thmc_model_versions(PROJECT_ID, storage=storage))

        ogs = submit_ogs_job(PROJECT_ID, model_version_id, "mesh-2d-cross-section-001", storage=storage)
        pflotran = submit_pflotran_job(PROJECT_ID, model_version_id, "mesh-2d-cross-section-001", storage=storage)
        responses.extend([ogs, pflotran])
        for submitted in (ogs, pflotran):
            job_id = submitted["results"][0]["job_id"]
            responses.append(get_compute_job_status(job_id, storage=storage))
            responses.append(fetch_compute_job_results(job_id, storage=storage))

        run = save_thmc_run_record(
            PROJECT_ID,
            "model-001",
            model_version_id,
            "PHREEQC",
            input_asset_ids=["phreeqc-input"],
            output_asset_ids=["phreeqc-output"],
            storage=storage,
        )
        run_id = run["results"][0]["run_id"]
        responses.append(run)
        responses.append(get_thmc_run_record(run_id, storage=storage))
        responses.append(list_thmc_run_records(PROJECT_ID, storage=storage))

        for response in responses:
            assert_response(response, response["tool"])
            if not response["ok"]:
                raise AssertionError(f"{response['tool']} failed unexpectedly: {response['errors']}")
            if response["mode"] != "mock":
                raise AssertionError(f"{response['tool']} should run in mock mode during smoke test")

        print(json.dumps({"ok": True, "tool_count": len({item["tool"] for item in responses}), "responses": len(responses)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
