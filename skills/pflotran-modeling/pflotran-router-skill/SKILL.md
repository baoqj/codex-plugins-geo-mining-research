---
name: pflotran-router-skill
description: Route GeoMine research questions to the independent PFLOTRAN Modeling skill family when field-scale reactive transport, 2D/3D groundwater simulation, long-term spatial prediction, THC modeling, or PFLOTRAN input deck generation is required.
---

# PFLOTRAN Router Skill

## Purpose

Decide whether PFLOTRAN is the right solver-specific workflow and choose the downstream PFLOTRAN skill chain.

## When To Use

Use for explicit PFLOTRAN requests, field/site/regional reactive transport, 2D/3D groundwater transport, long-term geochemical prediction, HPC-oriented subsurface simulation, THC modeling, mineral-reaction-driven porosity/permeability changes, and spatial outputs such as concentration fields, pH fields, mineral volume fractions, porosity fields, or breakthrough curves.

Do not use for single-water-sample speciation, saturation indices only, batch reaction screening, conceptual THMC with no solver selection, simple figures, or compliance-only questions.

## Required Inputs

Research objective, scenario, domain scale, dimensionality, known water chemistry, lithology/mineralogy, hydraulic/thermal data, boundary conditions, candidate reactions, expected outputs, and whether PHREEQC/THMC context already exists.

## Internal Workflow

1. Classify scenario: tailings seepage, uranium-series radionuclide transport, acid mine drainage, geothermal THC groundwater, CO2 storage, mining heat pollution, nuclear waste repository groundwater chemistry, or field-scale contaminant transport.
2. Decide whether PFLOTRAN is justified over PHREEQC or conceptual THMC.
3. Select downstream skills: conceptual model, grid/material, flow/transport, chemistry, THC, geomechanics, input deck, run management, output analysis, calibration/validation, paper synthesis.
4. List missing inputs and non-selected tools.
5. Require a PFLOTRAN Modeling Package.

## Output Contract

Return:

```json
{
  "use_pflotran": true,
  "reason": [],
  "scenario_classification": "",
  "selected_skill_chain": [],
  "not_selected_tools": [],
  "missing_inputs": []
}
```

## Handoff Rules

Hand off PHREEQC-only tasks to `phreeqc-modeling-skill`. Hand off solver-agnostic coupling tasks to `thmc-groundwater-router-skill`. Hand off justified PFLOTRAN solver work to this family.

## Limitations

Routing is not solver validation. Do not claim PFLOTRAN is optimal unless the comparison criteria are stated.
