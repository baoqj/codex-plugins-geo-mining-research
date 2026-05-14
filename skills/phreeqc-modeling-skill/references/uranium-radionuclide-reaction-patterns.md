# Uranium And Radionuclide Reaction Patterns

Use this reference for uranium mine groundwater, deep geological repository groundwater, and U-series transport screening.

## Common Questions

- Uranium aqueous speciation as carbonate, hydroxide, phosphate, sulfate, or fluoride complexes.
- Saturation indices for uraninite, schoepite, coffinite, calcite, gypsum, barite, ferrihydrite, and relevant host-rock minerals.
- Redox sensitivity of U(IV)/U(VI), Fe(II)/Fe(III), sulfate/sulfide, and dissolved oxygen.
- Radium behavior with barite/celestite/sulfate and ion exchange.
- Radon as a gas-phase or dissolved tracer only when data and boundary assumptions exist.

## PHREEQC Planning

- Start with `SOLUTION` and `SELECTED_OUTPUT`.
- Use `llnl.dat` or another documented database only after checking uranium/radionuclide species.
- Use `EQUILIBRIUM_PHASES` for hypothesis tests with explicit phase amounts.
- Use `SURFACE` or `EXCHANGE` only with documented site density, exchange capacity, and constants.
- Use `TRANSPORT` only when boundary conditions, geometry, dispersivity/diffusion, and initial states are known or explicitly placeholder-based.

## Guardrails

Do not infer radiological safety, repository performance, or regulatory compliance from a draft PHREEQC model. Treat redox state, adsorption constants, colloids, fracture flow, decay chains, and microbial effects as uncertainty sources unless measured or modeled explicitly.
