from __future__ import annotations

from geomine_thmc_mcp.storage import THMCStorage
from geomine_thmc_mcp.tools import (
    fetch_compute_job_results,
    get_compute_job_status,
    get_thmc_run_record,
    save_thmc_model_version,
    save_thmc_run_record,
    submit_ogs_job,
)


def test_model_version_compute_job_and_run_record_round_trip(tmp_path):
    storage = THMCStorage(cache_dir=tmp_path, mode="mock")
    model = save_thmc_model_version(
        "om-prj-uranium-001",
        "model-001",
        "v0.1",
        {"scenario": "uranium_mine_groundwater", "coupling_level": "THC"},
        storage=storage,
    )
    model_version_id = model["results"][0]["model_version_id"]
    job = submit_ogs_job("om-prj-uranium-001", model_version_id, "mesh-2d-cross-section-001", storage=storage)
    job_id = job["results"][0]["job_id"]
    assert get_compute_job_status(job_id, storage=storage)["results"][0]["status"] == "running"
    assert fetch_compute_job_results(job_id, storage=storage)["results"][0]["status"] == "completed"
    run = save_thmc_run_record(
        "om-prj-uranium-001",
        "model-001",
        model_version_id,
        "OGS",
        input_asset_ids=["mesh-2d-cross-section-001"],
        output_asset_ids=[f"{job_id}-results"],
        storage=storage,
    )
    run_id = run["results"][0]["run_id"]
    assert get_thmc_run_record(run_id, storage=storage)["results"][0]["solver"] == "OGS"
