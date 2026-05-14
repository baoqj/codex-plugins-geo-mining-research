"""Pure THMC MCP tool functions."""

from .project_database import list_openmine_projects, get_openmine_project, get_project_aoi
from .water_chemistry import query_water_chemistry_samples
from .lithology_mineralogy import query_lithology_units, query_mineral_assemblages
from .dgr_data_collection import (
    build_dgr_calibration_dataset,
    get_dgr_data_campaign,
    get_dgr_data_package,
    ingest_dgr_in_situ_stress,
    ingest_dgr_packer_test,
    ingest_dgr_rock_core_measurement,
    ingest_dgr_sensor_timeseries,
    ingest_dgr_water_sample,
    list_dgr_data_campaigns,
    list_dgr_data_packages,
    register_dgr_borehole,
    save_dgr_data_package,
    validate_dgr_thmc_dataset,
)
from .r2_postgis import get_thmc_mesh_catalog, fetch_mesh_or_parameter_field
from .phreeqc_service import build_phreeqc_input, run_phreeqc_job
from .remote_compute import submit_ogs_job, submit_pflotran_job, get_compute_job_status, fetch_compute_job_results
from .pflotran_modeling import (
    build_pflotran_input_deck,
    build_pflotran_result_summary,
    build_pflotran_run_manifest,
    get_pflotran_model_package,
    list_pflotran_model_packages,
    parse_pflotran_observation_output,
    save_pflotran_model_package,
    validate_pflotran_input_deck,
)
from .model_registry import save_thmc_model_version, get_thmc_model_version, list_thmc_model_versions
from .run_records import save_thmc_run_record, get_thmc_run_record, list_thmc_run_records

__all__ = [
    "list_openmine_projects",
    "get_openmine_project",
    "get_project_aoi",
    "query_water_chemistry_samples",
    "query_lithology_units",
    "query_mineral_assemblages",
    "list_dgr_data_campaigns",
    "get_dgr_data_campaign",
    "register_dgr_borehole",
    "ingest_dgr_sensor_timeseries",
    "ingest_dgr_water_sample",
    "ingest_dgr_rock_core_measurement",
    "ingest_dgr_packer_test",
    "ingest_dgr_in_situ_stress",
    "validate_dgr_thmc_dataset",
    "build_dgr_calibration_dataset",
    "save_dgr_data_package",
    "get_dgr_data_package",
    "list_dgr_data_packages",
    "get_thmc_mesh_catalog",
    "fetch_mesh_or_parameter_field",
    "build_phreeqc_input",
    "run_phreeqc_job",
    "submit_ogs_job",
    "submit_pflotran_job",
    "get_compute_job_status",
    "fetch_compute_job_results",
    "build_pflotran_input_deck",
    "validate_pflotran_input_deck",
    "build_pflotran_run_manifest",
    "parse_pflotran_observation_output",
    "build_pflotran_result_summary",
    "save_pflotran_model_package",
    "get_pflotran_model_package",
    "list_pflotran_model_packages",
    "save_thmc_model_version",
    "get_thmc_model_version",
    "list_thmc_model_versions",
    "save_thmc_run_record",
    "get_thmc_run_record",
    "list_thmc_run_records",
]
