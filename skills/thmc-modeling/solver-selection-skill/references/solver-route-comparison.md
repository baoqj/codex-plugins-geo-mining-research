# Solver Route Comparison

| Route | Best use | Strength | Limitation |
|---|---|---|---|
| PHREEQC | batch reactions, 1D reactive transport | strong geochemistry | weak THM |
| Python + PHREEQC / PhreeqcRM | prototypes, parameter scans | flexible and automatable | limited complex THMC |
| COMSOL + PHREEQC | complex multiphysics geometry | GUI and multiphysics | licensing and coupling complexity |
| OpenGeoSys + PHREEQC | open-source THMC research | reproducible geoscience THMC | learning curve |
| PFLOTRAN | large-scale reactive transport / HPC | scalable | setup and visualization effort |
| CrunchFlow / MIN3P | reactive transport research | mature RT modeling | availability and workflow constraints |
| PINN / PyTorch surrogate | inversion or surrogate modeling | AI workflow | must be benchmarked against physics model |

