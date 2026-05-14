# GeoMine Research User Manual

## 1. Overview

GeoMine Research is a Codex plugin for research-grade geoscience and mining workflows. It is designed for researchers, analysts, and developers who need structured reasoning around AOIs, geochemical data, mineral systems, academic papers, figures, groundwater chemistry, THMC modeling, PHREEQC, PFLOTRAN, and Canadian mining disclosure boundaries.

The plugin is not a black-box data service. It is a structured research operating system for Codex:

```text
Question -> entity normalization -> research type classification -> skill routing -> evidence lanes -> synthesis -> artifact generation
```

The plugin separates:

- evidence retrieval and provenance;
- interpretation and uncertainty;
- modeling package design;
- academic writing;
- visualization and PDF export;
- regulatory and disclosure caveats.

## 2. Design Principles

### Evidence Before Claims

Material claims must be traceable to a dataset, source, model, equation, user-provided file, or explicit placeholder. The plugin must not invent source IDs, assays, sample counts, map layers, model outputs, DOI values, or live retrieval results.

### Default-Off MCP

MCP servers are available as local implementations and examples, but they are disabled by default. This keeps Codex startup stable and makes live or mock mode explicit.

### Skill-First Modularity

Each skill has a narrow job. Routers select the minimum skill set needed for the task. This avoids turning one giant prompt into an opaque system.

### Academic Restraint

GeoMine can help write scientific papers, but it must avoid overstating causality, feasibility, safety, economic value, or regulatory conclusions.

### Reproducible Artifacts

When possible, outputs should preserve scripts, parameters, source versions, assumptions, and generated artifacts such as Markdown, PDF, JSON, figures, or model package files.

## 3. Core Architecture

GeoMine Research contains five layers:

1. Plugin metadata and documentation.
2. Skills for reasoning, writing, modeling, figures, and synthesis.
3. References and templates.
4. Deterministic helper scripts.
5. Optional MCP servers.

The router skills are the entrypoints:

- `geomine-research-router-skill`
- `research-router-skill`

They identify the task type, normalize entities, choose skill lanes, and preserve output boundaries.

## 4. Main Capability Groups

### 4.1 Base GeoMine Research

Use for AOI screening, source planning, geochemical interpretation, mineral occurrence context, deposit model fit, and disclosure-safe reports.

Typical skills:

- `aoi-crs-normalizer-skill`
- `geodata-discovery-skill`
- `geochemical-survey-skill`
- `mineral-occurrence-skill`
- `deposit-model-skill`
- `ni43-101-disclosure-check-skill`
- `report-synthesis-skill`

Example:

```text
Use GeoMine Research to screen a Saskatchewan AOI for uranium potential using public geology, geochemistry, mineral occurrence, and disclosure-safe caveats.
```

### 4.2 Academic Paper Writing

Use when the user asks for a research paper, journal article, formal report, literature-grounded mechanism paper, equations, hypotheses, or peer-review-ready draft.

Core flow:

```text
academic-geochemistry-paper-architect
  -> domain/model skills
  -> academic-paper-research-writer
  -> geomine-paper-pdf-export-skill
```

The geochemistry paper architect classifies the paper type before drafting:

- Data Paper / Database Paper
- Regional Geochemical Characterization Paper
- Mineral Exploration Geochemistry Paper
- Petrogenesis Paper
- Isotope Geochemistry Paper
- Hydrogeochemistry Paper
- Environmental Geochemistry Paper
- Reactive Transport Modelling Paper
- Experimental Geochemistry Paper
- Radiolysis / Nuclear Geochemistry Paper
- Geochemical Modelling and Machine Learning Paper
- Review / Perspective Paper
- Technical Note / Methods Paper

Example:

```text
Use GeoMine Research to design and draft a hydrogeochemistry paper on uranium migration in fractured Canadian Shield groundwater using PHREEQC speciation and saturation indices.
```

### 4.3 Figure Package and Visualization

Use `academic-figure-package-skill` for publication figure packages. It plans the figure set, figure inventory, visual grammar, captions, data/provenance requirements, and reproducible script scaffolds.

Use `geomine-visualization-studio-skill` for React/Vite/Three.js conceptual scenes such as:

- geologic basin margin;
- vein and fault systems;
- drillhole and stratigraphy scenes;
- research workflow scenes;
- geologic evolution animations.

Example:

```text
Use GeoMine Research to generate a 3D conceptual uranium basin-margin visualization page with stratigraphy, faults, drillholes, geochemical evidence lanes, provenance, and caveats.
```

### 4.4 PHREEQC Modeling

Use `phreeqc-modeling-skill` for standalone groundwater chemistry and geochemical reaction modeling plans.

Supported model types include:

- speciation;
- saturation index;
- batch reaction;
- equilibrium phases;
- kinetic reactions;
- surface complexation;
- ion exchange;
- gas phase;
- one-dimensional transport;
- inverse modeling;
- PhreeqcRM coupling plan.

The skill generates PHREEQC Modeling Packages, input templates, selected output plans, run manifests, methods text, missing-data lists, and uncertainty statements. It does not invent chemistry data, constants, mineral amounts, or calibration results.

### 4.5 THMC Modeling

The THMC family supports thermo-hydro-mechanical-chemical groundwater and reactive-transport research planning.

It can design:

- scenario classification;
- coupling level: H, HC, THC, HM, THM, THMC;
- conceptual model;
- governing equations;
- hydro-transport setup;
- geochemical reaction network;
- thermal transport;
- mechanical damage and porosity/permeability feedback;
- solver route;
- validation and sensitivity plan;
- THMC figures and report synthesis.

Core Mode does not require MCP. MCP-Enhanced Mode can use optional `geomine_thmc` and `geomine_thmc_data` when available.

### 4.6 PFLOTRAN Modeling

The PFLOTRAN family is independent from THMC but can receive THMC conceptual outputs.

It supports:

- conceptual model;
- input deck skeleton;
- grid and material plan;
- flow and transport plan;
- chemistry and reaction plan;
- THC coupling plan;
- geomechanics boundary notes;
- run management;
- output/observation analysis;
- calibration/validation;
- paper synthesis.

The optional `geomine_pflotran` MCP server is a planning layer. It does not execute PFLOTRAN by default.

## 5. MCP Operation Model

GeoMine has four optional MCP servers:

- `geomine`
- `geomine_thmc`
- `geomine_thmc_data`
- `geomine_pflotran`

They are configured through disabled example files:

- `references/geomine.mcp.example.json`
- `references/geomine-thmc.mcp.example.json`
- `references/geomine-thmc-data.mcp.example.json`
- `references/geomine-pflotran.mcp.example.json`

Important rules:

- Do not claim MCP was used unless a tool was actually called.
- Do not turn mock output into live evidence.
- Preserve `mode`, `provenance`, `warnings`, and `errors`.
- Keep secrets out of logs and prompts.

## 6. Installation and Local Use

Install as a local Codex plugin by copying or symlinking this folder into a plugin marketplace root, such as:

```text
~/.codex/plugins/geo-mining-research
```

Then install it through Codex. If using MCP, add the MCP server explicitly.

Validate the package:

```bash
python3 scripts/validate_plugin.py
PYTHONPATH=scripts uv run --no-project --with pytest --with "mcp[cli]>=1.2.0" --with "httpx>=0.28.0" python -m pytest
```

## 7. Example Workflows

### AOI Screening

```text
Use GeoMine Research to screen the Athabasca Basin margin for uranium potential. Include geology, geochemistry, mineral occurrences, evidence gaps, and NI 43-101-safe caveats.
```

Expected output:

- normalized AOI and jurisdiction;
- evidence lanes;
- source plan;
- deposit-model fit;
- confidence and gaps;
- safe next-work recommendations.

### Academic Geochemistry Paper

```text
Use GeoMine Research to write a geochemistry academic paper about carbonate-enhanced uranium migration in fractured groundwater. Use PHREEQC as the modeling method and export Markdown and PDF.
```

Expected output:

- paper type classification;
- research questions and hypotheses;
- data/method audit;
- PHREEQC package plan;
- evidence matrix;
- manuscript sections;
- formula-safe PDF export.

### THMC Modeling Package

```text
Use GeoMine Research THMC Modeling to build a THMC Modeling Package for sulfide tailings seepage, shallow groundwater transport, and pH buffering.
```

Expected output:

- scenario classification;
- active T/H/M/C processes;
- coupling level;
- governing equations;
- reaction network;
- solver route;
- validation/sensitivity plan;
- figure plan;
- modeling package.

### PFLOTRAN Modeling Package

```text
Use GeoMine Research to design a PFLOTRAN reactive transport model for uranium mobility in a 2D fractured aquifer.
```

Expected output:

- conceptual model;
- grid/material plan;
- flow/transport setup;
- chemistry blocks;
- input deck skeleton;
- output plan;
- run manifest;
- paper methods draft.

### Figure Package

```text
Use GeoMine Research to create a Figure Package for a uranium groundwater paper, including study area map, Piper diagram, Eh-pH diagram, saturation index plot, speciation plot, and conceptual migration cross-section.
```

Expected output:

- figure inventory;
- figure-by-figure specifications;
- axes, units, legends, source notes;
- script plans;
- captions;
- publication checklist.

## 8. Limitations

GeoMine Research does not provide:

- legal advice;
- investment advice;
- Qualified Person opinions;
- resource or reserve estimates;
- feasibility conclusions;
- permitting decisions;
- validated safety cases;
- live solver guarantees;
- automatically verified third-party datasets.

When data are missing, the plugin should use placeholders and explain how the gap affects interpretation.

## 9. Project Organization and Roadmap

The current cleanup strategy is:

- keep implemented skills and tested MCP layers;
- keep MCP default-off;
- group documentation under `docs/`;
- document mock/live boundaries clearly;
- avoid deleting useful draft capability files unless tests and docs confirm they are obsolete;
- improve public docs and portal access;
- continue converting source planners into bounded adapters only when reliable public interfaces are confirmed.

See [PROJECT_ORGANIZATION_PLAN.md](PROJECT_ORGANIZATION_PLAN.md).
