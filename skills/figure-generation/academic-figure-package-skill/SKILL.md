---
name: academic-figure-package-skill
description: Plan, specify, and validate publication-ready academic figure packages for research papers, including conceptual diagrams, workflows, data visualizations, GIS maps, geochemical figures, mining exploration figures, model architecture diagrams, and multi-panel figure layouts. Designed for GeoMine Research and general academic writing workflows.
---

# Academic Figure Package Skill

## Purpose

Use this skill as a paper figure design director. It turns a paper abstract, outline, research report, GeoMine evidence matrix, dataset description, or technical memo into a complete Figure Package: figure strategy, inventory, figure-by-figure specifications, visual grammar, prompts, script plans, captions, publication checks, and a JSON manifest.

The skill does not promise final journal-accepted artwork. It produces reproducible plans, editable prompts, script scaffolds, map layout checklists, captions, and validation reports for author and domain-expert review.

## When to use this skill

Use it when the user asks for paper figures, academic diagrams, scientific illustrations, graphical abstracts, figure plans, manuscript-ready captions, multi-panel layouts, GIS maps, geochemical anomaly figures, exploration workflow figures, radionuclide migration diagrams, or a publication-ready Figure Package.

Also use it when the user provides a paper abstract, paper outline, research proposal, GeoMine Research output, evidence matrix, or report draft and asks how to visualize the research.

## When not to use this skill

Do not use it for simple factual Q&A, ordinary report text, final legal/QP disclosure language, investment recommendations, resource/reserve validation, or one-off decorative image prompts unless the user asks for visualization.

## Required inputs

Minimum input:

- Paper or project title.
- Research question or main argument.
- Discipline and intended audience.
- Desired figure types or paper sections, if known.

Important optional inputs:

- Abstract, outline, methods, results, evidence matrix, or paper draft.
- AOI, CRS, map extent, layers, scale, and source metadata.
- Geochemical sample medium, units, detection limits, analytical method, and QA/QC status.
- Deposit model, commodity, project stage, and NI 43-101 context.
- Target journal, page width, color restrictions, and file-format requirements.

## Operating modes

- `full_package`: create the complete Figure Package.
- `inventory_only`: produce only the figure list and section mapping.
- `single_figure_spec`: design one figure in detail.
- `caption_pass`: draft or revise figure captions.
- `script_scaffold`: generate Mermaid, Matplotlib, or QGIS layout scaffolds.
- `publication_check`: validate an existing package or figure plan.

## Figure Package workflow

Step 1. Figure Intent Classification.

Classify each figure as one or more of: problem-framing figure, study-area figure, method-workflow figure, experimental-design figure, conceptual-mechanism figure, data-visualization figure, GIS / map figure, geochemical-anomaly figure, model-architecture figure, evidence-synthesis figure, technical-report figure, graphical abstract.

Step 2. Figure Inventory Planning.

Plan the full paper figure set. Map each figure to a paper section, main message, required data, and output format.

Step 3. Scientific Content Decomposition.

Break each figure into entities, processes, relationships, data layers, variables, uncertainties, and caveats.

Step 4. Figure Type Selection.

Choose among schematic diagram, flowchart, cross-section, map, multi-panel figure, scatter plot, box plot, heatmap, Piper diagram, Eh-pH diagram, Sankey diagram, evidence matrix, model architecture diagram, and other justified types.

Step 5. Visual Grammar Design.

Define color, line style, arrow meaning, shapes, symbols, fonts, panel labels, legends, uncertainty marks, and caveat marks. Use redundant encoding beyond color.

Step 6. Panel Layout Planning.

Plan single-panel or multi-panel figures. Multi-panel plans must define panel labels, panel purpose, reading order, relative size, and shared legends.

Step 7. Toolchain Recommendation.

Recommend lightweight reproducible tools first: Mermaid or Graphviz for workflows, Python Matplotlib/R ggplot2 for data plots, GeoPandas/QGIS for maps, SVG/Inkscape/Figma/Illustrator for final vector editing, and GeoMine Visualization Studio for conceptual 3D or web scenes.

Step 8. Drawing Prompt / Script Plan Generation.

Produce a drawing prompt, Mermaid/DOT scaffold, Matplotlib scaffold, QGIS layout checklist, or figure production plan. Keep AI image generation as a sketching aid only.

Step 9. Caption Drafting.

Draft captions that state what the figure shows, panel meanings, data sources, method summary, symbols, color/abbreviation meanings, and caveats.

Step 10. Publication Readiness Check.

Check panel labels, font consistency, legends, accessible colors, source metadata, map requirements, reproducibility, output formats, and caveats.

## Figure type taxonomy

See `references/figure-types.md` for the supported taxonomy. Use the taxonomy to select intent before selecting visual style.

## GeoMine-specific figure types

The skill supports:

- Study area and claim location map.
- Geological setting map.
- Sampling location map.
- Geological cross-section.
- Geochemical anomaly map.
- Pathfinder element association diagram.
- Radionuclide decay-chain and migration mechanism diagram.
- Groundwater flow and contaminant transport conceptual model.
- Eh-pH / hydrogeochemical condition diagram.
- Deposit model schematic.
- Exploration workflow diagram.
- Mineral prospectivity evidence matrix.
- Claim-neighbor and company-intelligence map.
- NI 43-101 technical disclosure review figure.
- GeoMine AI workflow architecture figure.

## Visual grammar rules

Read `references/visual-grammar.md` and `references/color-accessibility.md` when designing the package. Keep one cross-figure grammar. Example GeoMine conventions:

- Blue arrows: groundwater flow.
- Red dashed arrows: contaminant or radionuclide migration.
- Gray blocks: host rock or bedrock.
- Orange zones: geochemical anomaly.
- Purple zones: uranium-related radiological signal.
- Dotted line: inferred boundary.
- Solid line: observed boundary.
- Circles: sampling sites.
- Triangles: mineral occurrences.

## Toolchain selection rules

Use the simplest reproducible tool that fits the figure:

- Conceptual diagram: SVG, Figma, Inkscape, Illustrator.
- Workflow diagram: Mermaid, Graphviz, draw.io.
- Data plot: Python Matplotlib, R ggplot2, Plotly.
- GIS map: QGIS, GeoPandas, ArcGIS.
- Model architecture: Mermaid, Graphviz, Figma.
- Final layout: Inkscape, Illustrator, Affinity Designer.

Do not require GUI software in the skill workflow. GUI tools can be recommended as optional final-editing tools.

## Data visualization rules

For data figures, preserve dataset name, source, version, units, transformations, filters, missing-data treatment, uncertainty, and code path. Do not infer sample counts or results that were not provided.

## GIS map figure rules

Every GIS or map figure must include CRS, scale bar, north arrow, legend, data source, map extent, layer date or version where known, spatial precision, and limitations. If these are missing, mark them as required before final rendering.

## Geochemistry figure rules

Every geochemistry figure must include sample medium, units, analytical method, detection limits or censored-data handling, anomaly threshold method, QA/QC limitation, and compatible-survey warning when relevant.

## Mining exploration and NI 43-101 caveats

Do not imply mineral resources, reserves, economic value, feasibility, permitting status, QP opinion, or investment suitability from a figure package. Technical-report or mining disclosure figures must include data limitations and professional review caveats.

## Caption rules

See `references/caption-writing-rules.md`. Each caption must identify the figure purpose, panel meanings, source/provenance, method summary, symbol and color meanings, and limitations.

## Publication readiness checklist

Use `references/publication-checklist.md` and `templates/publication-checklist-template.md`. Check vector/raster format, resolution, color accessibility, font consistency, source provenance, reproducible scripts, map metadata, and caveats.

## Output contract

Return Markdown using this structure:

```markdown
# Figure Package: [Paper / Project Title]

## 1. Figure Strategy
## 2. Figure Inventory
## 3. Figure Specifications
### Figure 1. [Title]
#### Intent
#### Scientific Content
#### Visual Grammar
#### Layout Plan
#### Toolchain
#### Drawing Prompt
#### Script / Rendering Plan
#### Caption Draft
#### Publication Checklist
## 4. Cross-Figure Visual Consistency
## 5. Data and Provenance Requirements
## 6. Caveats
## 7. Machine-Readable JSON Summary
```

Also provide or save a JSON manifest following `templates/figure-manifest-template.json` when the user asks for files or machine-readable output.

## JSON schema

Use `templates/figure-manifest-template.json` as the manifest schema-style template. Every figure should include figure id, title, paper section, type, main message, scientific content, visual grammar, layout, toolchain, drawing prompt, script plan, caption draft, provenance requirements, publication checklist, and caveats.

## Integration with GeoMine Research skills

- Use `geomine-research-router-skill` or `research-router-skill` to classify the research task and evidence lanes.
- Use `academic-paper-research-writer` before this skill when the paper structure, hypotheses, equations, and evidence matrix are not yet defined.
- Use `geodata-discovery-skill` before map figures when source and layer metadata are missing.
- Use `geochemical-survey-skill` before geochemistry figures when sample medium, units, thresholds, or QA/QC are unclear.
- Use `ni43-101-disclosure-check-skill` for technical disclosure, resource/reserve wording, project economics, or investor-facing mining materials.
- Use `geomine-visualization-studio-skill` when the package needs a 3D conceptual web scene or staged visual research demo.

## Examples

See:

- `examples/uranium-groundwater-figure-package.md`.
- `examples/geochemical-anomaly-map-figure-package.md`.
- `examples/mining-project-study-area-map-package.md`.
- `examples/geomine-ai-workflow-figure-package.md`.
