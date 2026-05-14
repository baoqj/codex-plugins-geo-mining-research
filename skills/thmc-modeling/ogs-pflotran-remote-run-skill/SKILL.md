---
name: ogs-pflotran-remote-run-skill
description: Prepare, submit, monitor, and record OpenGeoSys or PFLOTRAN THMC remote-compute jobs through geomine_thmc MCP when available, with Core Mode fallback to job specifications and reproducibility checklists.
---

# OGS / PFLOTRAN Remote Run Skill

## Purpose

Convert a THMC Modeling Package and model version into job-based OpenGeoSys or PFLOTRAN execution artifacts, then collect job status, output assets, and run records.

## Mode Selection

- MCP-Enhanced Mode: use `get_thmc_mesh_catalog`, `fetch_mesh_or_parameter_field`, `save_thmc_model_version`, `submit_ogs_job` or `submit_pflotran_job`, `get_compute_job_status`, `fetch_compute_job_results`, and `save_thmc_run_record`.
- Core Mode: produce a solver-ready job specification without claiming execution.
- Remote compute must be job-based; do not present long-running solver work as synchronous unless the MCP tool explicitly returns completed output.

## Solver Routing

- Prefer OGS when the study emphasizes groundwater flow, transport, heat transport, mechanics, and OpenGeoSys-PHREEQC style coupling.
- Prefer PFLOTRAN when the study emphasizes large-scale reactive transport, HPC execution, and structured result packages.
- Keep PHREEQC-alone workflows in `phreeqc-coupling-skill`.

## Output Contract

Return:

- Solver choice and reason.
- Model version id.
- Mesh and parameter-field asset ids.
- Job submission payload summary.
- Job id, status, and result asset ids.
- Run record payload with solver version, input assets, output assets, parameter hash, data hash, warnings, and error log.

## Guardrails

Do not claim numerical convergence, calibration, safety, compliance, or regulatory validity unless the solver output and validation evidence are supplied and reviewed. MCP job success is not scientific validation.
