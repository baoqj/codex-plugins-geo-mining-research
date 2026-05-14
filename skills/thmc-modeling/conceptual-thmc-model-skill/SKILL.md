---
name: conceptual-thmc-model-skill
description: Convert groundwater chemistry, mining environmental, radionuclide, tailings, geothermal, or repository research problems into conceptual THMC models with domain, boundaries, processes, assumptions, exclusions, and coupling matrix drafts.
---

# Conceptual THMC Model Skill

## Purpose

Create the conceptual model that all later THMC work depends on. Define the system, domain, geometry, boundaries, active processes, observations, assumptions, excluded processes, and the first coupling matrix.

## Inputs

- Research objective and scenario.
- Geological units, fractures, tailings, waste rock, repository barrier, aquifer, or geothermal system.
- Spatial scale, time scale, observation points, and available data.
- Active T/H/M/C processes from `thmc-groundwater-router-skill`.

## Workflow

1. Define model purpose: explanatory, screening, benchmark, design support, or publication.
2. Define domain: 1D column, 2D cross-section, 3D domain, or fractured network.
3. Identify geological units, hydrogeological pathways, reaction zones, heat sources, mechanical features, and observation points.
4. Separate observed data from conceptual inference.
5. List dominant processes and excluded processes.
6. Draft a coupling matrix using `templates/coupling-matrix-template.md`.
7. Produce a conceptual diagram specification for `thmc-paper-figure-skill` or `academic-figure-package-skill`.

## Supported Scenarios

- Uranium-series radionuclide migration.
- Acid mine drainage.
- Tailings seepage.
- Bentonite buffer evolution.
- Geothermal water-rock interaction.
- Fractured rock contaminant transport.

## Output Contract

Return:

- System narrative.
- Model domain and geometry.
- Geological units.
- Hydrogeological pathways.
- Thermal conditions.
- Mechanical features.
- Chemical reaction zones.
- Observation points.
- Dominant and excluded processes.
- Assumptions.
- Conceptual diagram specification.
- Coupling matrix draft.

