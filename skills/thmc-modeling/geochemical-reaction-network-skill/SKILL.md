---
name: geochemical-reaction-network-skill
description: Design scenario-specific groundwater geochemical reaction networks for THMC reactive transport, including uranium-series radionuclides, acid mine drainage, tailings seepage, bentonite buffer evolution, geothermal water-rock interaction, sorption, redox, mineral reactions, and PHREEQC-style draft blocks.
---

# Geochemical Reaction Network Skill

## Purpose

Translate groundwater chemistry and geochemical processes into a reaction network suitable for PHREEQC, PFLOTRAN, OpenGeoSys-PHREEQC, COMSOL-PHREEQC, or custom reactive transport modeling.

## Scenario Networks

Use the matching reference:

- Uranium-series radionuclide migration: `references/uranium-series-reaction-network.md`.
- Acid mine drainage: `references/acid-mine-drainage-reaction-network.md`.
- Tailings seepage: `references/tailings-seepage-reaction-network.md`.
- Bentonite buffer / nuclear waste: `references/bentonite-buffer-reaction-network.md`.
- Geothermal water-rock interaction: `references/geothermal-water-rock-reaction-network.md`.

## Output Contract

Return:

- Aqueous species table.
- Mineral phases table.
- Gas phases if relevant.
- Redox couples.
- Kinetic reactions.
- Sorption / surface complexation / ion exchange models.
- Required thermodynamic database.
- Missing data list.
- PHREEQC-style draft blocks, clearly marked as draft.
- MCP tool plan: whether to call `build_phreeqc_input` and `run_phreeqc_job`, and which water samples, minerals, database, and reaction-network fields should be supplied.
- Mock/live mode warning when the reaction-network artifacts come from `geomine_thmc`.

## Guardrails

Do not invent thermodynamic constants, kinetic rates, distribution coefficients, or radionuclide half-lives. Use placeholders and required-data flags unless values are supplied or verified.
