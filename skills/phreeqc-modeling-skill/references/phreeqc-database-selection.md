# PHREEQC Database Selection

Choose the database before writing model interpretation. Database choice is a scientific assumption because species, phases, reactions, and constants differ.

## Common Databases

| Database | Good use | Cautions |
| --- | --- | --- |
| `phreeqc.dat` | Major ions, carbonate systems, simple saturation indices, teaching examples | Limited trace-metal/radionuclide coverage |
| `wateq4f.dat` | Natural-water speciation and trace elements in WATEQ-style workflows | Check species and minerals for the exact elements used |
| `llnl.dat` | Broad thermodynamic coverage and exploratory trace/radionuclide modeling | Large database; reactions may not be internally consistent for every specialized system |
| `minteq.dat` / `minteq.v4.dat` | Environmental trace metals, adsorption, surface complexation workflows | Surface constants and site definitions must match the model |
| `pitzer.dat` | High-salinity brines and evaporitic systems | Only use for supported species/interactions |
| `sit.dat` | Saline systems using SIT activity corrections | Coverage may be narrower than the study requires |
| `Amm.dat`, `ColdChem.dat`, `frezchem.dat` | Specialized ammonia/cold/low-temperature chemistry | Use only when scenario matches the database scope |

## Selection Workflow

1. List target species, minerals, surfaces, gases, and redox couples.
2. Check whether the database contains them.
3. Check activity model suitability for ionic strength.
4. Check whether surface/kinetic/exchange constants are database-compatible.
5. Document missing phases/species and how that limits interpretation.
6. Avoid undocumented database merging.

## Reporting Language

Report the selected database by filename and path when known. Explain why it is adequate for the stated model objective and where it is incomplete.
