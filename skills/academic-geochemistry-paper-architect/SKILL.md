---
name: academic-geochemistry-paper-architect
description: Design rigorous geochemistry academic paper architectures by classifying paper type, framing research questions and hypotheses, planning data, methods, figures, tables, uncertainty, citation discipline, and downstream GeoMine skills before drafting.
---

# Academic Geochemistry Paper Architect

## Purpose

Use this skill before drafting geochemistry-related papers. It converts a topic into a paper architecture that is problem-driven, data-constrained, method-transparent, mechanism-oriented, figure-supported, and bounded by uncertainty.

This skill is an architect, not a generic report writer. It controls paper structure and writing logic so GeoMine Research produces doctoral or postdoctoral-style geochemistry papers instead of broad surveys.

## When To Use

Use this skill when the user asks for a paper, article, proposal, outline, manuscript, revision, methods section, figure plan, or academic writing strategy involving:

- whole-rock, soil, sediment, groundwater, isotope, radiogenic, stable-isotope, radiolysis, radionuclide, mineral exploration, environmental, or hydrogeochemical data;
- PHREEQC, saturation indices, speciation, reaction paths, reactive transport, THMC chemistry, PFLOTRAN chemistry, or geochemical modeling;
- geochemical anomaly interpretation, prospectivity, regional characterization, petrogenesis, crustal evolution, database papers, methods papers, reviews, or perspectives.

If the user asks for final prose, use this skill first to build the architecture, then hand off to `academic-paper-research-writer`. If the paper has equations or PDF output, finish with `geomine-paper-pdf-export-skill`.

## Core Workflow

1. Classify the topic into primary, secondary, and optional tertiary geochemistry paper types using `references/paper-type-taxonomy.md`.
2. Restate the scientific problem, knowledge gap, research questions, and testable hypotheses.
3. Audit available and missing data. Do not invent sample counts, concentrations, model results, datasets, references, software versions, thermodynamic constants, or boundary conditions.
4. Select methods, models, and downstream GeoMine skills. Use `phreeqc-modeling-skill`, THMC, PFLOTRAN, GIS, figure, or PDF skills only when justified by the topic.
5. Build the figure and table architecture. Every figure must support a claim, have units and provenance requirements, and be referenced by a paper section.
6. Generate a section-level paper outline and writing controls. Keep Results observational; put interpretation, mechanisms, alternatives, and implications in Discussion.
7. Add citation requirements, uncertainty checks, academic restraint rules, and a final quality checklist.

## Paper Types

Classify into one or more of:

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

Mixed papers are common. State the primary type and explain how secondary types change the outline.

## Writing Logic

Enforce this chain:

```text
Scientific problem -> knowledge gap -> testable hypotheses -> data design -> methods -> results -> mechanism -> alternative explanations -> uncertainty -> implications
```

Do not let available data alone define the paper. The paper must answer a scientific question.

## Output Contract

Return Markdown with:

1. Paper type classification and rationale.
2. Recommended writing mode: data paper, regional characterization, exploration, petrogenesis, isotope, hydrogeochemistry, environmental, reactive-transport, experimental, nuclear/radiolysis, modeling/ML, review/perspective, or methods note.
3. Scientific problem, knowledge gap, research questions, and hypotheses.
4. Required data checklist and missing-data impact.
5. Methods and modeling plan with reproducibility requirements.
6. Figure architecture and table plan.
7. Detailed paper outline with section-level writing instructions.
8. Citation and reference requirements.
9. Uncertainty, limitation, and alternative-explanation checklist.
10. Academic quality checklist.
11. Downstream GeoMine skill routing plan.

Use `templates/geochemistry-paper-architecture-template.md` for the full package format. Use `scripts/generate_paper_architecture.py` when a deterministic first-pass architecture is useful.

## Guardrails

- Do not fabricate measured values, sample counts, locations, model outputs, thermodynamic constants, kinetic constants, citations, DOI values, or calibration results.
- Distinguish measured, modeled, inferred, illustrative, and literature-derived claims.
- Do not write correlation as causation without independent mechanistic evidence.
- Do not infer economic mineralization, feasibility, or reserve/resource conclusions from geochemical evidence alone.
- Every key claim needs a source, method, model, dataset, or explicit placeholder.
- Every conclusion must trace back to the evidence matrix and acknowledge boundary conditions.

## Reference Loading

- Use `references/paper-type-taxonomy.md` for classification rules and type-specific structures.
- Use `references/section-writing-rules.md` when drafting or revising section instructions.
- Use `references/data-method-qaqc-rules.md` for data audit, QA/QC, transformations, and reproducibility.
- Use `references/figure-table-architecture.md` for geochemistry figure/table planning.
- Use `references/citation-uncertainty-guardrails.md` for citations, uncertainty, limitations, and academic restraint.
