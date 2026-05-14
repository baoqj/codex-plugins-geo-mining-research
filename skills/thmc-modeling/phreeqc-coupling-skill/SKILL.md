---
name: phreeqc-coupling-skill
description: Build PHREEQC-ready chemistry inputs and mock/live PHREEQC run requests for GeoMine THMC Modeling Package workflows, using geomine_thmc MCP tools when available and falling back to draft blocks when MCP is unavailable.
---

# PHREEQC Coupling Skill

## Purpose

Turn water chemistry, mineral assemblages, redox assumptions, sorption concepts, and reaction-network outputs into PHREEQC coupling artifacts for THMC research workflows.

## Mode Selection

- MCP-Enhanced Mode: if `geomine_thmc` is available, call `query_water_chemistry_samples`, `query_mineral_assemblages`, `build_phreeqc_input`, and optionally `run_phreeqc_job`.
- Core Mode: if MCP is unavailable, draft PHREEQC blocks from user-provided chemistry and label them as unexecuted drafts.
- Never hide mock mode. If MCP returns `mode: "mock"`, repeat that status in the modeling package.

## Workflow

1. Confirm scenario, model id, chemical species, thermodynamic database, and units.
2. Collect water chemistry with QA/QC flags and detection limits.
3. Collect mineral phases and reactive surface-area gaps.
4. Build a draft PHREEQC input and mark database/species assumptions.
5. Run PHREEQC only when requested or when the workflow requires a smoke-test output.
6. Record every input asset, output asset, warning, and missing thermodynamic parameter.

## Output Contract

Return:

- PHREEQC database choice and caveats.
- Sample-to-SOLUTION mapping.
- Aqueous totals, redox placeholders, minerals, sorption/ion-exchange placeholders.
- Draft PHREEQC input or MCP `phreeqc_input` asset id.
- PHREEQC job id and selected-output summary if executed.
- Warnings about unit conversion, charge balance, species mapping, and mock/live mode.

## Guardrails

Do not invent thermodynamic constants, decay constants, kinetic rates, adsorption constants, or validated speciation results. A successful PHREEQC mock run only validates workflow shape.
