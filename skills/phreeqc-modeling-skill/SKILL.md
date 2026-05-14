---
name: phreeqc-modeling-skill
description: Design PHREEQC geochemical models from groundwater chemistry, lithology, mineralogy, and THMC context; generate PHREEQC input files, selected-output plans, run manifests, and paper-ready methods/results guidance without inventing measurements or constants.
---

# PHREEQC Modeling Skill

## Purpose

Use this skill to convert GeoMine research ideas, groundwater chemistry tables, lithology/mineralogy observations, and THMC context into a reproducible PHREEQC modeling package. The package should classify the model type, audit the available input data, recommend a database, plan PHREEQC keywords, generate `.phr` input fragments, describe run instructions, design selected output, and draft paper-ready methods/results language.

This skill can run independently from THMC Modeling. When a broader THMC task needs PHREEQC, the THMC router may call this skill as a downstream chemistry modeling specialist.

## When To Use

Use this skill when the user requests PHREEQC, geochemical speciation, saturation indices, water-rock reaction, acid mine drainage reactions, uranium/radionuclide groundwater chemistry, tailings seepage chemistry, inverse geochemical modeling, or a PhreeqcRM coupling plan.

Also use it when the user provides groundwater chemistry data and asks for interpretation that depends on pH, Eh/pe, alkalinity, major ions, trace metals, mineral equilibrium, sorption, ion exchange, gas phase, kinetic reactions, or reactive transport.

Do not use this skill for generic mineral exploration summaries unless geochemical modeling is requested.

## Model Type Classification

Classify the request into one or more supported model types:

- `speciation`
- `saturation_index`
- `batch_reaction`
- `equilibrium_phases`
- `kinetic_reactions`
- `surface_complexation`
- `ion_exchange`
- `gas_phase`
- `one_dimensional_transport`
- `inverse_modeling`
- `PhreeqcRM_coupling_plan`

Select the smallest model type that answers the research question. Escalate from speciation/saturation-index screening to reactions, transport, or coupling only when the question requires that process.

## Input Data Audit Workflow

Before writing PHREEQC input, audit the supplied data:

1. Identify sample IDs, locations/depths, sampling dates, field parameters, analytical method, units, detection limits, QA/QC, and charge-balance fields if available.
2. Separate measured data from assumptions, literature constants, placeholders, and model choices.
3. Verify units for pH, temperature, pe/Eh, alkalinity, major ions, trace elements, dissolved gases, isotope/radionuclide activities, mineral amounts, surface-site density, exchange capacity, and kinetic rates.
4. List missing data and how each missing field affects interpretation.
5. Use explicit placeholders such as `<Ca_mg_L>`, `<pe_or_Eh>`, `<Calcite_initial_moles>`, and `<rate_constant_source>` when data are not provided.

Never invent measured concentrations, kinetic constants, surface complexation constants, thermodynamic data, mineral amounts, calibration results, or field boundary conditions.

Use `scripts/validate_water_chemistry_table.py` for local CSV/JSON audits when a chemistry table is provided.

## Database Selection Rules

Use the detailed guide in `references/phreeqc-database-selection.md` when database choice matters.

Default rules:

- `phreeqc.dat`: conservative default for major-ion speciation, carbonate equilibria, and simple saturation-index screening.
- `wateq4f.dat`: common for natural-water major ions and trace elements where WATEQ-style aqueous speciation is expected.
- `llnl.dat`: broad thermodynamic coverage; use cautiously for trace metals/radionuclides and document species/database limitations.
- `minteq.dat` or `minteq.v4.dat`: use when surface complexation, adsorption, or trace-metal environmental chemistry is central and constants are compatible with the chosen surface model.
- `pitzer.dat`: use for high-ionic-strength brines where Pitzer interaction terms are needed.
- `sit.dat`: consider for specific-ion-interaction modeling in saline systems when supported species are adequate.

Do not merge databases casually. If a mineral/species/constant is missing, report it and propose a documented extension workflow rather than fabricating a reaction.

## PHREEQC Keyword Planning Rules

Use `references/phreeqc-keywords.md` for keyword details. Plan only the keywords justified by the input data and objective.

Common mappings:

- Speciation or saturation index: `SOLUTION`, `SELECTED_OUTPUT`, optional `USER_PUNCH`.
- Batch water-rock reaction: `SOLUTION`, `REACTION`, optional `EQUILIBRIUM_PHASES`.
- Mineral equilibrium: `EQUILIBRIUM_PHASES`.
- Kinetics: `KINETICS`, `RATES`, `INCREMENTAL_REACTIONS`.
- Surface complexation: `SURFACE`, optional `SURFACE_MASTER_SPECIES` and `SURFACE_SPECIES` only when constants are documented.
- Ion exchange: `EXCHANGE`, optional `EXCHANGE_MASTER_SPECIES` and `EXCHANGE_SPECIES` only when documented.
- Gas phase: `GAS_PHASE`.
- One-dimensional transport: `TRANSPORT`, `SOLUTION` zones, optional `KINETICS`, `EXCHANGE`, `SURFACE`.
- Inverse modeling: `INVERSE_MODELING`, measured initial/final waters, phases, uncertainty ranges.
- PhreeqcRM coupling plan: define cell chemistry, database, selected outputs, reaction modules, transport solver interface, state variables, and update frequency; do not claim a live coupled run unless it was executed.

## Input File Generation Rules

Generate `.phr` input as a draft model artifact, not as proof of validity. Prefer template fragments from `templates/` and script output from `scripts/`.

Rules:

- Preserve units exactly. Convert only when the user asks and the conversion is explicit.
- Use PHREEQC comments (`#`) to mark assumptions and placeholders.
- Include `TITLE`, `SOLUTION`, and `END` in every runnable draft.
- Use `SELECTED_OUTPUT` for every model so results can be parsed.
- Keep `DATABASE` selection outside the `.phr` file in the run manifest and run instructions.
- Use `-charge` only when charge balancing is intended and documented.
- Mark all uncertain redox handling, alkalinity basis, density, gas exchange, mineral amounts, and boundary conditions.

## Run Instruction Rules

If PHREEQC is installed, run with:

```bash
phreeqc input.phr output.out database.dat
```

If the local macOS install is used in this environment, the wrapper is expected at:

```bash
~/.local/bin/phreeqc input.phr output.out ~/.local/phreeqc/phreeqc-3.5.0-14000/database/phreeqc.dat
```

When PHREEQC is not installed, provide install guidance and still generate the modeling package. Do not claim model results unless a run actually completed.

Use `scripts/make_phreeqc_run_manifest.py` to record input, output, database, PHREEQC executable, checksums, model type, and objective.

## Selected Output Design Rules

Use `templates/selected-output-template.phr` or `scripts/generate_selected_output.py`.

At minimum include pH, pe, temperature, alkalinity, ionic strength, charge balance, and water. Add:

- `-totals` for major ions, trace elements, uranium/radionuclides, sulfate, carbonate, Fe, Al, Mn, and metals relevant to the question.
- `-saturation_indices` for minerals used in interpretation.
- `-molalities` or `-activities` only for species needed to support a paper argument.
- `USER_PUNCH` only when calculations require custom derived values.

## Paper Writing Guidance

Use `templates/paper-methods-template.md` and `references/phreeqc-paper-methods-writing.md`.

Paper-ready output should include:

- Research objective and model scope.
- Justification for database selection.
- Input chemistry table provenance and QA/QC limits.
- PHREEQC keyword plan and reason for each process.
- Explicit assumptions and placeholders.
- Run command, PHREEQC version/path, database path, input/output filenames, and selected output design.
- Interpretation plan separating model setup, executed results, and hypotheses.
- Limitations on thermodynamic coverage, redox disequilibrium, kinetics, adsorption constants, inverse-model non-uniqueness, and boundary conditions.

## Future MCP Extension

Do not implement a live PHREEQC MCP server in this skill. For future MCP work, define these tools:

- `run_phreeqc`
- `validate_phreeqc_input`
- `parse_phreeqc_output`
- `save_model_version`
- `query_water_samples`
- `query_mineralogy`

Until those tools exist, use local files and scripts only. If an MCP tool is unavailable, state that the skill is operating in local-only mode.

## Required Output

Return a PHREEQC Modeling Package with:

1. Research objective.
2. Model type classification.
3. Input data audit.
4. Database recommendation.
5. PHREEQC keyword plan.
6. Generated input.
7. Run instructions.
8. Selected output design.
9. Interpretation plan.
10. Paper methods draft.
11. Limitations and uncertainty.
12. Future MCP extension, if relevant.

## Limitations And Uncertainty Rules

PHREEQC output is a geochemical calculation, not a field validation. Always distinguish:

- measured field/lab data,
- literature thermodynamic/kinetic constants,
- database choices,
- placeholders,
- model assumptions,
- calculated speciation/saturation indices,
- calibrated parameters,
- unvalidated hypotheses.

Never present a PHREEQC model as regulatory proof, a Qualified Person opinion, a reserve/resource statement, an engineering design, or a validated environmental compliance result without independent professional review and real data.
