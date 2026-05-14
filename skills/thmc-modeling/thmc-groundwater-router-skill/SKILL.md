---
name: thmc-groundwater-router-skill
description: Route groundwater chemistry and reactive transport research questions into the GeoMine THMC Modeling skill family by classifying scenarios, detecting active T/H/M/C processes, selecting coupling level, choosing downstream skills, and requesting a THMC Modeling Package.
---

# THMC Groundwater Router Skill

## Purpose

Determine whether a research problem requires THMC groundwater chemistry modeling. Classify the scenario, identify active Thermal/Hydrological/Mechanical/Chemical processes, select the coupling level, choose downstream THMC skills, and require a final THMC Modeling Package.

## Trigger Scenarios

Recognize these scenario labels:

- `acid_mine_drainage`
- `radionuclide_transport`
- `uranium_mine_groundwater`
- `tailings_seepage`
- `nuclear_waste_repository`
- `bentonite_buffer_evolution`
- `geothermal_fluid_rock_interaction`
- `co2_storage_reactive_transport`
- `fractured_rock_contaminant_transport`
- `mining_heat_pollution`
- `groundwater_metal_mobility`
- `long_term_environmental_risk`
- `reactive_transport_benchmark`
- `custom_thmc_model`

## Coupling Level Rules

- `H`: flow only; no chemistry requested.
- `HC`: groundwater flow plus solute or reactive transport.
- `THC`: temperature affects flow, transport, or reactions, with no explicit mechanics.
- `HM`: flow plus mechanics, such as pore pressure, effective stress, fracture aperture, or permeability.
- `THM`: heat plus flow plus mechanics, with no chemistry focus.
- `THMC`: full coupling including chemistry and mechanical feedback.

Do not force full THMC. Choose the smallest coupling level that answers the research question.

## Active Process Detection

- Thermal is active for temperature, thermal gradient, geothermal, heat pollution, waste heat, thermal expansion, temperature-dependent reaction, or high-temperature water-rock interaction.
- Hydrological is active for groundwater flow, seepage, recharge, hydraulic gradient, pore pressure, saturation, diffusion, dispersion, advection, fracture flow, or contaminant transport.
- Mechanical is active for stress, strain, deformation, fracture aperture, permeability evolution, porosity evolution, swelling, damage, compaction, subsidence, effective stress, or geomechanics.
- Chemical is active for water chemistry, geochemical reaction, pH, Eh, ions, minerals, adsorption, desorption, ion exchange, surface complexation, dissolution, precipitation, redox, radioactive decay, sulfate, carbonate, uranium, radium, radon, lead, polonium, metals, or PHREEQC.

## Downstream Skill Selection

Always consider:

- `conceptual-thmc-model-skill`
- `governing-equations-skill`
- `hydro-transport-skill`
- `geochemical-reaction-network-skill` when chemical is active
- `thermal-gradient-heat-transport-skill` when thermal is active
- `mechanical-damage-permeability-skill` when mechanical is active or optional mechanical feedback matters
- `solver-selection-skill`
- `reactive-transport-implementation-skill`
- `dgr-field-data-acquisition-skill` when the task mentions DGR, deep geological repository, nuclear waste repository, bentonite buffer, Revell-style repository setting, boreholes, packer tests, in-situ stress, field monitoring, or现场实测数据
- `phreeqc-modeling-skill` when the user requests PHREEQC, provides groundwater chemistry data, or asks for speciation, saturation indices, water-rock reaction, inverse modeling, reaction network testing, geochemical input generation, selected output parsing, or a PhreeqcRM coupling plan
- `phreeqc-coupling-skill` when chemical speciation, reaction-network testing, or PHREEQC draft/run artifacts are needed
- Independent `pflotran-modeling` family handoff when solver selection recommends PFLOTRAN for field-scale reactive transport, 2D/3D spatial simulation, long-term geochemical prediction, THC simulation, or HPC execution
- `ogs-pflotran-remote-run-skill` when mesh assets, OGS/PFLOTRAN job submission, job status, result assets, or run records are needed
- `calibration-validation-skill`
- `uncertainty-sensitivity-skill`
- `thmc-paper-figure-skill` when figures or publication output are needed
- `thmc-report-synthesis-skill` for final package assembly

## MCP-Enhanced Mode

Use Core Mode by default when MCP tools are unavailable. If the `geomine_thmc` MCP server is available, use it only as an evidence and execution layer:

- project and AOI context: `list_openmine_projects`, `get_openmine_project`, `get_project_aoi`
- chemistry and geology inputs: `query_water_chemistry_samples`, `query_lithology_units`, `query_mineral_assemblages`
- mesh and fields: `get_thmc_mesh_catalog`, `fetch_mesh_or_parameter_field`
- chemistry execution: `build_phreeqc_input`, `run_phreeqc_job`
- remote compute: `submit_ogs_job`, `submit_pflotran_job`, `get_compute_job_status`, `fetch_compute_job_results`
- reproducibility: `save_thmc_model_version`, `save_thmc_run_record`

If the `geomine_thmc_data` MCP server is available, use it as the DGR field-data acquisition layer:

- campaign context: `list_dgr_data_campaigns`, `get_dgr_data_campaign`
- borehole and monitoring inputs: `register_dgr_borehole`, `ingest_dgr_sensor_timeseries`
- field/lab data: `ingest_dgr_water_sample`, `ingest_dgr_rock_core_measurement`, `ingest_dgr_packer_test`, `ingest_dgr_in_situ_stress`
- data readiness: `validate_dgr_thmc_dataset`, `build_dgr_calibration_dataset`
- reproducibility: `save_dgr_data_package`, `get_dgr_data_package`, `list_dgr_data_packages`

Every MCP result must keep its `mode`, `provenance`, `warnings`, and `errors` in the final THMC Modeling Package. Mock MCP output may demonstrate workflow shape but not scientific validity.

## PHREEQC Routing Rules

Call `phreeqc-modeling-skill` before final THMC synthesis when:

- the user explicitly requests PHREEQC;
- the user provides groundwater chemistry, porewater, seepage, monitoring-well, hydrochemistry, or water-quality data;
- the user asks for speciation, saturation index, water-rock reaction, mineral equilibrium, inverse modeling, ion exchange, surface complexation, gas phase, one-dimensional transport, or PhreeqcRM;
- the geochemical reaction network needs a runnable PHREEQC input draft, database choice, selected output design, or paper-ready PHREEQC methods text.

The PHREEQC skill can run independently from THMC. Use it as a downstream chemistry modeler and keep its PHREEQC Modeling Package inside the THMC Modeling Package. Do not claim a live PHREEQC MCP execution unless an actual tool or local command was run.

## Handoff To PFLOTRAN

When the THMC solver-selection step recommends PFLOTRAN for reactive transport or THC simulation, hand off to the independent `skills/pflotran-modeling/pflotran-router-skill`.

Use PFLOTRAN when the problem requires field-scale or regional reactive transport, 2D/3D groundwater simulation, long-term spatial geochemical prediction, HPC execution, mineral-reaction feedback on porosity/permeability, or spatial outputs such as concentration, pH, mineral volume, porosity fields, and breakthrough curves.

Do not treat PFLOTRAN as a child skill under THMC; PFLOTRAN is not a child skill under THMC. THMC provides the scientific coupling framework; PFLOTRAN provides the solver-specific implementation package.

## Required Router Output

Return a planning JSON before synthesis:

```json
{
  "research_type": "radionuclide_transport",
  "scenario": "uranium_mine_groundwater",
  "coupling_level": "THC",
  "active_processes": {
    "thermal": true,
    "hydrological": true,
    "mechanical": false,
    "chemical": true
  },
  "recommended_skills": [],
  "required_outputs": [
    "THMC Modeling Package",
    "MCP status table",
    "DGR field-data acquisition and data-gap matrix",
    "coupling matrix",
    "reaction network",
    "solver route",
    "model version / run record plan",
    "validation plan",
    "figure plan",
    "machine-readable JSON model spec"
  ],
  "fallback_mode": "skills-only",
  "mcp_enhanced_mode": {
    "server": "geomine_thmc",
    "data_server": "geomine_thmc_data",
    "use_if_available": true,
    "required": false
  }
}
```

## Guardrails

This skill creates a modeling plan, not a validated numerical simulation. Do not claim engineering certification, environmental compliance, regulatory approval, feasibility, or investment value. State data gaps and professional-review needs.
