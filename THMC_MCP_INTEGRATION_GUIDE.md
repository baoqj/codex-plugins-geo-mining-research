# GeoMine THMC MCP Integration Guide

## Purpose

`geomine_thmc` is an optional MCP server for THMC Skill Family 2.0. It adds structured data access, PHREEQC input/job scaffolding, OGS/PFLOTRAN job lifecycle tools, model-version storage, and run-record storage.

`geomine_thmc_data` is the companion optional MCP server for DGR field-data acquisition. It handles campaign metadata, boreholes, sensor time series, packer tests, groundwater chemistry, rock-core measurements, in-situ stress, THMC coverage validation, calibration dataset packaging, and DGR data package records.

`geomine_pflotran` is an optional PFLOTRAN planning MCP server. It handles draft PFLOTRAN input deck generation/validation, run manifests, observation-output parsing, result summaries, and PFLOTRAN Modeling Package records. It does not execute PFLOTRAN in v0.1.

THMC skills must still work in Core Mode when this server is not installed or not enabled.

## Server

```text
server name: geomine_thmc
command: uv --directory ./mcp/geomine-thmc-server run geomine-thmc-mcp
default mode: mock

server name: geomine_thmc_data
command: uv --directory ./mcp/geomine-thmc-server run geomine-thmc-data-mcp
default mode: mock

server name: geomine_pflotran
command: uv --directory ./mcp/geomine-thmc-server run geomine-pflotran-mcp
default mode: mock
```

The plugin keeps these servers disabled by default. Use `references/geomine-thmc.mcp.example.json`, `references/geomine-thmc-data.mcp.example.json`, and `references/geomine-pflotran.mcp.example.json` as activation templates.

## Tool Groups

| Group | Tools |
|---|---|
| Project database | `list_openmine_projects`, `get_openmine_project`, `get_project_aoi` |
| Chemistry | `query_water_chemistry_samples` |
| Geology/mineralogy | `query_lithology_units`, `query_mineral_assemblages` |
| Mesh/assets | `get_thmc_mesh_catalog`, `fetch_mesh_or_parameter_field` |
| PHREEQC | `build_phreeqc_input`, `run_phreeqc_job` |
| Remote compute | `submit_ogs_job`, `submit_pflotran_job`, `get_compute_job_status`, `fetch_compute_job_results` |
| Registry | `save_thmc_model_version`, `get_thmc_model_version`, `list_thmc_model_versions`, `save_thmc_run_record`, `get_thmc_run_record`, `list_thmc_run_records` |
| DGR field-data acquisition | `list_dgr_data_campaigns`, `get_dgr_data_campaign`, `register_dgr_borehole`, `ingest_dgr_sensor_timeseries`, `ingest_dgr_water_sample`, `ingest_dgr_rock_core_measurement`, `ingest_dgr_packer_test`, `ingest_dgr_in_situ_stress`, `validate_dgr_thmc_dataset`, `build_dgr_calibration_dataset`, `save_dgr_data_package`, `get_dgr_data_package`, `list_dgr_data_packages` |
| PFLOTRAN planning | `validate_input_deck`, `build_input_deck`, `build_run_manifest`, `parse_observation_output`, `generate_result_summary`, `save_model_package`, `get_model_package`, `list_model_packages` |

## Response Contract

Every tool returns:

```json
{
  "ok": true,
  "mode": "mock",
  "tool": "tool_name",
  "query": {},
  "results": [],
  "assets": [],
  "provenance": {},
  "warnings": [],
  "errors": []
}
```

Do not discard `mode`, `provenance`, `warnings`, or `errors` when writing a THMC Modeling Package.

## Workflow

1. Route the research problem with `thmc-groundwater-router-skill`.
2. Use Core Mode if MCP is unavailable.
3. If MCP is available, fetch project context, water chemistry, lithology/mineralogy, and mesh assets.
4. For DGR or field-data-heavy tasks, use `dgr-field-data-acquisition-skill` and `geomine_thmc_data` before calibration design.
5. Use `phreeqc-coupling-skill` for PHREEQC artifacts.
6. For solver-specific PFLOTRAN package work, hand off to the independent `pflotran-modeling` family and use `geomine_pflotran` only for planning artifacts, not live execution.
7. Use `ogs-pflotran-remote-run-skill` for job submission/status/results.
8. Save a model version before remote compute.
9. Save DGR data packages and run records when datasets or solver jobs are created.
10. Synthesize all artifacts into THMC Modeling Package 2.0.

## Live Mode Requirements

Live mode is not enabled by default. Future live adapters should require explicit environment variables and must never print secrets:

```text
OPENMINE_API_BASE_URL
OPENMINE_API_TOKEN
OPENMINE_PROJECT_DB_URL
OPENMINE_POSTGIS_DSN
OPENMINE_R2_ENDPOINT
OPENMINE_R2_ACCESS_KEY_ID
OPENMINE_R2_SECRET_ACCESS_KEY
OPENMINE_R2_BUCKET
PHREEQC_SERVICE_URL
PHREEQC_SERVICE_TOKEN
THMC_COMPUTE_API_URL
THMC_COMPUTE_API_TOKEN
```
