# Figure Package: GeoMine Research Plugin Workflow and Evidence Synthesis

## 1. Figure Strategy

- Paper section: system architecture, methods, outputs.
- Research purpose: explain how GeoMine Research routes geoscience questions through evidence lanes, optional MCP tools, skills, synthesis, figure packages, visualizations, and PDF export.
- Main visual argument: the plugin is a provenance-aware research workflow, not an automatic mining decision system.
- Target audience: AI research, geoscience informatics, mining data systems.
- Target journal or format: white paper, academic methods article, or plugin documentation.
- Discipline profile: AI agents, geoscience data, mining research workflows.

## 2. Figure Inventory

| Figure | Type | Paper Section | Main Message | Required Data | Output Format |
|---|---|---|---|---|---|
| Figure 1 | Workflow architecture | Methods | Research router selects focused evidence lanes | plugin architecture | SVG/PDF |
| Figure 2 | Evidence lane matrix | Methods | Evidence lanes preserve provenance and uncertainty | skill list, tool list | PDF/SVG |
| Figure 3 | Optional MCP architecture | Implementation | MCP is optional and default-off | MCP config, tools | SVG/PDF |
| Figure 4 | Output pipeline | Results | Outputs include papers, PDFs, figures, visualizations | output contracts | SVG/PDF |

## 3. Figure Specifications

### Figure 1. GeoMine research-router workflow

#### Intent

Method-workflow figure and model-architecture figure.

#### Scientific Content

- Entities: user prompt, research router, domain skills, evidence matrix, synthesis.
- Processes: normalize entities, classify task, plan evidence lanes, synthesize output.
- Relationships: router coordinates skills and evidence boundaries.
- Data layers: plugin skills, evidence contracts, user files, optional tools.
- Variables: research type, AOI, commodity, output format.
- Uncertainties: MCP availability and source completeness.
- Caveats: not a decision engine.

#### Visual Grammar

Blue = user/research flow; gray = skill modules; purple = optional visualization; dotted boxes = optional components; labels distinguish evidence from inference.

#### Layout Plan

Left-to-right workflow from user prompt to outputs.

#### Toolchain

Primary tool: Mermaid or Graphviz. Secondary tool: Inkscape. Export formats: SVG/PDF.

#### Drawing Prompt

Create a clean architecture workflow showing prompt intake, GeoMine research router, domain evidence lanes, synthesis, academic paper writing, figure package design, visualization, and PDF export.

#### Script / Rendering Plan

Use Mermaid scaffold with nodes for prompt, router, evidence lanes, synthesis, output.

#### Caption Draft

**Figure 1. GeoMine research-router workflow.** The workflow shows how GeoMine Research classifies a user question, normalizes entities, selects evidence lanes, and synthesizes outputs. Optional tools are marked with dotted boundaries.

#### Publication Checklist

- [ ] Skill modules and optional components distinguished.
- [ ] No claim of autonomous mining decision-making.
- [ ] Source/provenance boundary shown.

### Figure 2. Evidence lanes and provenance matrix

#### Intent

Evidence-synthesis figure and model-architecture figure.

#### Scientific Content

- Entities: AOI, GIS, geochemistry, occurrences, deposit models, NI 43-101, literature, outputs.
- Processes: evidence grading, provenance capture, caveat propagation.
- Relationships: each lane contributes claims and limitations.
- Data layers: source metadata, confidence, limitations.
- Variables: evidence grade, source type, uncertainty.
- Uncertainties: static versus live retrieval.
- Caveats: source recommendations are not retrieved evidence unless queried.

#### Visual Grammar

Rows = evidence lanes; columns = source, method, output, caveat; hatching = unavailable data; icons = MCP, local file, model inference.

#### Layout Plan

Matrix panel with legend and caveat note.

#### Toolchain

Primary tool: Python Matplotlib table or SVG. Export formats: PDF/SVG.

#### Drawing Prompt

Create an evidence lane matrix for GeoMine Research showing GIS, geochemistry, occurrences, deposit model, compliance, academic writing, figure package, visualization, and PDF export lanes.

#### Script / Rendering Plan

Render from a static table listing lane, source type, output, confidence, and caveat.

#### Caption Draft

**Figure 2. Evidence lanes and provenance matrix.** The matrix summarizes GeoMine Research evidence lanes and how provenance, confidence, and caveats are preserved across outputs.

#### Publication Checklist

- [ ] Evidence and inference separated.
- [ ] Provenance fields shown.
- [ ] Caveats visible.

### Figure 3. Optional MCP and default-off plugin architecture

#### Intent

Model-architecture figure and technical workflow figure.

#### Scientific Content

- Entities: Codex plugin, local skills, optional geomine MCP server, scripts, public data adapters.
- Processes: manual MCP enablement, tool invocation, provenance-preserving output.
- Relationships: MCP is an optional data layer, not a hard dependency.
- Data layers: MCP config, tool list, adapter skeletons.
- Variables: enabled tools, command, environment.
- Uncertainties: local installation and live-source availability.
- Caveats: default-off behavior avoids startup failures.

#### Visual Grammar

Solid boxes = always-available source templates; dotted boxes = optional MCP; lock icon or label = manual enablement; arrows = data flow.

#### Layout Plan

Three-column architecture: Codex plugin, optional MCP server, outputs.

#### Toolchain

Primary tool: Mermaid/Graphviz. Export formats: SVG/PDF.

#### Drawing Prompt

Create an architecture diagram showing GeoMine plugin skills, optional geomine MCP server, data adapters, and outputs. Mark MCP as default-off and manually enabled.

#### Script / Rendering Plan

Use Mermaid with dotted optional MCP subgraph.

#### Caption Draft

**Figure 3. Optional MCP and default-off plugin architecture.** The diagram shows local GeoMine skills and optional MCP tools. MCP is not required for the Figure Package skill and remains manually enabled.

#### Publication Checklist

- [ ] Default-off MCP boundary shown.
- [ ] Does not imply live retrieval unless tools are invoked.
- [ ] No hidden dependency on external GUI software.

### Figure 4. Report, paper, figure, visualization, and PDF output pipeline

#### Intent

Method-workflow figure and output-synthesis figure.

#### Scientific Content

- Entities: report synthesis, academic paper writer, figure package skill, visualization skill, PDF exporter.
- Processes: Markdown source, figure planning, script scaffolds, 3D demo generation, formula-safe PDF export.
- Relationships: Figure Package complements paper writing and visualization, rather than replacing them.
- Data layers: output contracts, figure manifest, markdown, PDF.
- Variables: output format and validation status.
- Uncertainties: final artwork and domain review remain external.
- Caveats: final figures require author and expert review.

#### Visual Grammar

Pipeline arrows; document icons; purple for visualization; green for validation status with labels and symbols, not color alone.

#### Layout Plan

Single pipeline panel with optional branches for PDF and 3D visualization.

#### Toolchain

Primary tool: Mermaid or SVG. Export formats: SVG/PDF.

#### Drawing Prompt

Create a publication pipeline diagram showing Markdown research output, academic paper writing, figure package planning, visualization generation, formula-safe PDF export, and validation reports.

#### Script / Rendering Plan

Use Mermaid workflow scaffold and export as SVG for final editing.

#### Caption Draft

**Figure 4. Report, paper, figure, visualization, and PDF output pipeline.** The figure summarizes how GeoMine Research transforms evidence into Markdown, academic papers, figure packages, visual demos, and PDF outputs while preserving caveats.

#### Publication Checklist

- [ ] Output artifacts and validation steps shown.
- [ ] Final expert review boundary included.
- [ ] Not a claim of automated final publication artwork.

## 4. Cross-Figure Visual Consistency

Use blue for research flow, gray for skills, purple for visualization, dotted boundaries for optional components, and direct labels for accessibility.

## 5. Data and Provenance Requirements

Record plugin version, skill names, optional MCP tools, output contracts, validation scripts, and whether any live tool was invoked.

## 6. Caveats

This package is documentation and research workflow planning. It is not legal advice, not investment advice, not a Qualified Person opinion, and not an automated final-publication claim.

## 7. Machine-Readable JSON Summary

```json
{
  "figure_package": {
    "title": "GeoMine Research Plugin Workflow and Evidence Synthesis",
    "paper_title": "GeoMine Research plugin workflow",
    "discipline": "geoscience AI workflow",
    "target_journal": "white paper or methods article",
    "created_for": "GeoMine Research",
    "figures": [
      {"figure_id": "Figure 1", "title": "GeoMine research-router workflow", "figure_type": "method-workflow figure"},
      {"figure_id": "Figure 2", "title": "Evidence lanes and provenance matrix", "figure_type": "evidence-synthesis figure"},
      {"figure_id": "Figure 3", "title": "Optional MCP and default-off plugin architecture", "figure_type": "model-architecture figure"},
      {"figure_id": "Figure 4", "title": "Report, paper, figure, visualization, and PDF output pipeline", "figure_type": "method-workflow figure"}
    ]
  }
}
```
