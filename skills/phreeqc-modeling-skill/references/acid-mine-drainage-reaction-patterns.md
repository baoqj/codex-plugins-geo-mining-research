# Acid Mine Drainage Reaction Patterns

Use this reference for sulfide oxidation, acidic drainage, metal mobility, and neutralization modeling.

## Typical Process Set

- Sulfide oxidation producing acidity, sulfate, Fe, Al, and metals.
- Fe(II)/Fe(III) redox and hydrolysis.
- Neutralization by calcite, dolomite, silicates, or alkalinity additions.
- Secondary mineral precipitation: ferrihydrite, goethite, schwertmannite, jarosite, gypsum, and metal hydroxides/sulfates.
- Adsorption or surface complexation on Fe-Al oxyhydroxides if constants are documented.

## PHREEQC Planning

- Start with measured acid drainage `SOLUTION`.
- Use `SOLUTION` plus `SELECTED_OUTPUT` for speciation and saturation index.
- Use `REACTION` for controlled neutralization or acid addition scenarios.
- Use `EQUILIBRIUM_PHASES` for phase-buffering hypotheses.
- Use `KINETICS` only with sourced pyrite oxidation/neutralization kinetics.
- Use `SURFACE` only with documented surface model and site density.

## Key Outputs

- pH, pe/Eh handling, alkalinity, sulfate, Fe, Al, Mn, major cations, trace metals.
- Saturation indices for carbonate, sulfate, Fe oxyhydroxide, and jarosite-family minerals.
- Charge balance and ionic strength.

## Guardrails

Do not invent pyrite abundance, oxygen flux, rate constants, alkalinity addition, or field seepage rates. If those are unknown, use placeholders and interpret outputs as scenario design only.
