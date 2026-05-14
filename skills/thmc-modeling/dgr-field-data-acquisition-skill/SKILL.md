---
name: dgr-field-data-acquisition-skill
description: Plan and call the GeoMine THMC DGR field-data acquisition MCP for deep geological repository THMC studies, including boreholes, sensor time series, packer tests, groundwater chemistry, rock-core thermal/mechanical data, in-situ stress, dataset validation, calibration datasets, and data packages.
---

# DGR Field Data Acquisition Skill

## Purpose

Use this skill when a THMC research task needs DGR-specific现场实测数据, calibration evidence, or data-gap assessment before modeling. The skill turns a conceptual THMC problem into a structured field-data acquisition and MCP-call plan.

## Mode Selection

- MCP-Enhanced Mode: if `geomine_thmc_data` is available, call DGR acquisition tools and preserve their `mode`, `provenance`, `warnings`, and `errors`.
- Core Mode: if MCP is unavailable, produce a data acquisition plan and required-data matrix without claiming records were collected.
- Mock mode must remain explicit. Mock/local records demonstrate schema and workflow shape only.

## Tool Map

Use `geomine_thmc_data` tools as follows:

- Campaign context: `list_dgr_data_campaigns`, `get_dgr_data_campaign`
- Borehole control: `register_dgr_borehole`
- Thermal/hydraulic monitoring: `ingest_dgr_sensor_timeseries`
- Chemistry/isotopes: `ingest_dgr_water_sample`
- Rock core tests: `ingest_dgr_rock_core_measurement`
- Hydraulic testing: `ingest_dgr_packer_test`
- Mechanical stress: `ingest_dgr_in_situ_stress`
- Coverage and gaps: `validate_dgr_thmc_dataset`
- Calibration package: `build_dgr_calibration_dataset`
- Reproducibility: `save_dgr_data_package`, `get_dgr_data_package`, `list_dgr_data_packages`

## Required Data Domains

Collect or request:

- Site and borehole metadata: collar, depth datum, deviation survey, lithological intervals, fracture zones.
- Thermal: temperature logs, thermal conductivity, heat capacity, geothermal gradient.
- Hydrological: hydraulic head, packer-test K/T values, pressure recovery, fracture transmissivity.
- Mechanical: in-situ stress, UCS/triaxial tests, elastic moduli, fracture aperture or deformation monitoring.
- Chemical: pH, Eh, EC/TDS, major ions, trace metals/radionuclides, isotopes, gas composition, microbial indicators if relevant.
- QA/QC: calibration certificates, duplicate/blank/reference samples, chain-of-custody, lab methods, detection limits, units, coordinate and depth reference.

## Workflow

1. Determine whether the scenario is DGR, nuclear waste repository, bentonite buffer evolution, deep fractured rock contaminant transport, or repository safety-interface research.
2. List or create the campaign context.
3. Register boreholes and depth references before ingesting depth-indexed measurements.
4. Ingest available T/H/M/C field measurements.
5. Run `validate_dgr_thmc_dataset` to produce a process coverage matrix and data-gap list.
6. Build a calibration dataset only after records have enough QA/QC metadata for the intended model stage.
7. Save a DGR data package when the dataset will feed a THMC Modeling Package, PHREEQC plan, OGS/PFLOTRAN plan, figure package, or academic paper.

## Output Contract

Return:

- MCP availability and mode.
- Campaign and borehole registry summary.
- T/H/M/C measurement inventory.
- QA/QC and provenance table.
- Data-gap matrix.
- Calibration dataset asset ids, if built.
- Data package id, if saved.
- Explicit caveats separating measured, mock, planned, inferred, and missing data.

## Guardrails

Do not fabricate field measurements. Do not convert mock/local ingestion into claims of DGR site characterization. Do not claim safety, compliance, licensing readiness, repository suitability, or validated THMC calibration from data collection alone.
