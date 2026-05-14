# Citation, Uncertainty, and Academic Restraint Guardrails

## Citation Discipline

Every key judgment needs a source or explicit placeholder. Cite:

- datasets and database versions;
- analytical methods and classification diagrams;
- formulas and normalization constants;
- prior models and regional geology;
- software, packages, PHREEQC databases, and thermodynamic data;
- experimental parameters and kinetic constants.

Use the journal style selected by the user:

- Elsevier / GCA: author-year.
- Nature / Science: numbered.
- ACS: numbered or ACS style.
- Earth System Science Data: author-year.
- Geochemical Perspectives Letters: author-year.

## Uncertainty

Always include an uncertainty or limitations section covering relevant items:

- spatial sampling bias;
- age uncertainty;
- analytical error;
- inconsistent source databases;
- lithology classification error;
- weathering and alteration;
- detection limits and censored data;
- duplicate-sample handling;
- model parameter uncertainty;
- thermodynamic database limitations;
- missing validation samples;
- machine-learning overfitting;
- correlation versus causation.

## Academic Restraint

Avoid over-extrapolation:

Bad: `The local U anomaly proves that the basin has high uranium potential.`

Better: `The observed U anomaly indicates local enrichment under the sampled geological and hydrogeochemical conditions. Broader extrapolation requires additional spatial coverage and independent geophysical or drilling constraints.`

Avoid correlation-as-causation:

Bad: `U correlates with HCO3, so HCO3 caused U migration.`

Better: `The positive U-HCO3 relationship, together with speciation modelling showing dominant U(VI)-carbonate complexes, is consistent with carbonate-enhanced U mobility.`

Always discuss alternatives such as lithology background, weathering, hydrothermal alteration, sampling bias, analytical error, metamorphic overprint, and hydrological mixing.
