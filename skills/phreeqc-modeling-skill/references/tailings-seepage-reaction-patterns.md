# Tailings Seepage Reaction Patterns

Use this reference for tailings porewater, seepage plumes, attenuation, and downstream groundwater impacts.

## Typical Process Set

- Tailings porewater chemistry evolves from sulfide oxidation, neutralization, evapoconcentration, and flushing.
- Seepage mixes with shallow groundwater.
- Carbonate/silicate buffering affects pH and alkalinity.
- Secondary minerals and Fe-Al oxyhydroxides affect metal mobility.
- Adsorption, ion exchange, and surface complexation may matter if site data exist.

## PHREEQC Planning

- Use separate `SOLUTION` blocks for porewater, background groundwater, and mixed seepage.
- Use `MIX` for simple end-member mixing when proportions are known or explicitly scenario-based.
- Use `EQUILIBRIUM_PHASES` for buffering/mineral-control hypotheses.
- Use `TRANSPORT` only when hydraulic boundary conditions and geometry are available.
- Use `INVERSE_MODELING` only with measured upstream/downstream waters and phase candidates.

## Key Outputs

- pH, alkalinity, sulfate, carbonate, major ions, Fe, Al, Mn, trace metals.
- Saturation indices for calcite/dolomite, gypsum, ferrihydrite/goethite, jarosite-family phases, and relevant metal phases.
- Interpretation of attenuation as a hypothesis, not proof, unless calibrated against field data.

## Guardrails

Do not infer seepage flux, plume extent, attenuation capacity, or compliance status without field data and hydrogeologic constraints.
