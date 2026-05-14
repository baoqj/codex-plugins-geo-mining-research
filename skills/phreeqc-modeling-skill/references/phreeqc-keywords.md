# PHREEQC Keyword Planning Reference

Use this file when translating a research question into PHREEQC blocks.

## Core Keywords

- `TITLE`: short model title and scenario identifier.
- `SOLUTION`: aqueous composition, temperature, pH, pe/Eh proxy, units, density, alkalinity, redox couples, and element totals.
- `END`: terminates a simulation block.
- `SELECTED_OUTPUT`: tabular output for parsing, plotting, and paper tables.
- `USER_PUNCH`: custom columns written to selected output.

## Speciation And Saturation

- Use `SOLUTION` plus `SELECTED_OUTPUT`.
- Add `-saturation_indices` for minerals relevant to the hypothesis.
- Add `-totals`, `-molalities`, or `-activities` only when they answer a stated question.

## Reactions And Equilibria

- `REACTION`: adds or removes a fixed amount of reactant; appropriate for simple titration or water-rock addition scenarios.
- `EQUILIBRIUM_PHASES`: equilibrates with phases at target saturation index and available phase amount.
- Use explicit placeholders for unknown mineral amounts.

## Kinetics

- `RATES`: Basic-language rate expression.
- `KINETICS`: named kinetic reactants, parameters, initial moles, steps.
- `INCREMENTAL_REACTIONS`: controls whether reaction increments are cumulative.
- Do not invent rate constants or reactive surface areas.

## Surface Complexation

- `SURFACE`: site definitions and initial surface state.
- `SURFACE_MASTER_SPECIES` and `SURFACE_SPECIES`: only when adding documented custom surface reactions.
- Do not mix surface models or constants without citing the source and database compatibility.

## Ion Exchange

- `EXCHANGE`: exchanger sites and initial composition.
- `EXCHANGE_MASTER_SPECIES` and `EXCHANGE_SPECIES`: only when documented custom exchange species are needed.
- Require CEC or exchange site capacity; otherwise use placeholders and list the gap.

## Gas Phase

- `GAS_PHASE`: fixed pressure or fixed volume gas equilibrium.
- Useful for CO2, O2, H2S, CH4, H2, or radon gas scenarios when gas boundary conditions are known.

## Transport

- `TRANSPORT`: one-dimensional advection/dispersion configuration.
- Requires cells, shifts, time step, lengths, dispersivity, diffusion, boundary solution, and initial solution distribution.
- Can combine with `KINETICS`, `EQUILIBRIUM_PHASES`, `SURFACE`, or `EXCHANGE`.
- Do not invent field boundary conditions or calibration results.

## Inverse Modeling

- `INVERSE_MODELING`: candidate phases and mass-balance constraints between measured initial/final waters.
- Requires uncertainty handling. Interpret solutions as non-unique hypotheses.

## PhreeqcRM Coupling Plan

- Not a PHREEQC keyword block by itself.
- Specify database, cell chemistry initialization, selected output mapping, reaction module state variables, coupling interval, transport solver responsibilities, and restart/versioning plan.
