# THMC Modeling Skill Family

THMC Modeling is an advanced GeoMine Research skill family for designing thermo-hydro-mechanical-chemical groundwater chemistry and reactive transport models.

It is not a validated numerical solver. It is a research modeling workflow that transforms a scientific problem into a structured THMC Modeling Package, including conceptual model, coupling map, equations, variables, reaction network, PHREEQC coupling plan, OGS/PFLOTRAN job plan, validation plan, uncertainty plan, figure plan, model version, run records, and machine-readable model specification.

Standalone PHREEQC design now lives in `skills/phreeqc-modeling-skill/`. The THMC router calls that skill when groundwater chemistry, speciation, saturation indices, water-rock reaction, inverse modeling, selected output, or PhreeqcRM planning are needed.

Core Mode:

- skills-only
- no MCP required
- uses bundled references, templates, and user-provided files

MCP-Enhanced Mode:

- optional `geomine_thmc` MCP server
- optional `geomine_thmc_data` MCP server for DGR field-data acquisition
- OpenMine project/AOI/water-chemistry/lithology/mineralogy lookup
- DGR campaign, borehole, sensor, packer-test, groundwater chemistry, rock-core, and in-situ stress records
- R2/PostGIS-style mesh and parameter-field asset lookup
- PHREEQC input builder and mock/live PHREEQC job shape
- OGS/PFLOTRAN job submit/status/result tools
- model-version and run-record registry

MCP output is an evidence and execution layer, not a substitute for scientific validation. Mock outputs must remain labelled as mock in final reports.
