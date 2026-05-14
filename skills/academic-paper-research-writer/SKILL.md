---
name: academic-paper-research-writer
description: Convert GeoMine Research topics into publication-oriented academic paper workflows with research framing, literature synthesis, mechanisms, equations, evidence matrices, citation discipline, limitations, peer review checks, and optional PDF export.
---

# Academic Paper Research Writer

## Purpose

Use this skill to turn a GeoMine Research topic into a formal academic paper workflow rather than a generic research report. It supports geoscience, geochemistry, mining, groundwater systems, radiation chemistry, porous media, mineral exploration, nuclear waste disposal, and environmental engineering topics.

The skill emphasizes precise research questions, hypotheses, literature positioning, mechanistic reasoning, equation-level rigor, evidence hierarchy, uncertainty, citation discipline, and publication-style writing.

## When To Use

Use this skill when the user asks for:

- academic paper, research article, journal paper, publication-ready draft, 投稿, 论文, 学术论文;
- abstract, keywords, literature review, research questions, hypotheses, theoretical framework, methods, discussion, limitations, references;
- formula derivation, governing equations, symbol table, units, boundary conditions, or peer-review-style quality checking;
- a GeoMine topic that should become a formal paper rather than a market report, technical memo, or broad survey.

Do not use it as the primary skill for business plans, market analysis, short explainers, news summaries, code design docs, or investment advice unless the user explicitly requests academic-paper format.

## Workflow

1. Load `prompts/system.md` for global behavior and use the smallest additional prompt files needed:
   - research framing: `prompts/research_framing.md`;
   - literature review: `prompts/literature_review.md`;
   - mechanisms: `prompts/mechanistic_reasoning.md`;
   - equations: `prompts/equation_derivation.md`;
   - evidence: `prompts/evidence_synthesis.md`;
   - writing: `prompts/academic_writing.md`;
   - citation discipline: `prompts/citation_style.md`;
   - peer review: `prompts/peer_review_check.md`.
2. Validate user intent against `schemas/input.schema.json`. Infer defaults when fields are missing.
3. First produce a paper plan: title, paper type, object, scope, questions, hypotheses, contribution, novelty, evidence needs, and limitations.
4. If the paper is geochemistry-specific, first use `academic-geochemistry-paper-architect` to classify the paper type and lock the paper architecture: scientific problem, knowledge gap, hypotheses, data requirements, methods, figure/table plan, section-level writing controls, uncertainty, and citation discipline.
5. If the paper requires GeoMine data, route through the existing GeoMine router and domain skills before writing:
   - AOI/CRS/GIS and source discovery for spatial papers;
   - geochemistry and deposit model skills for anomaly or mineral-system papers;
   - visualization skill for figures or conceptual 3D scenes;
   - paper PDF export skill after Markdown writing.
6. Build an evidence matrix before the final draft. Separate literature, equations, datasets, simulations, experiments, and inference.
7. Build an equation registry when equations are included. Every equation needs variables, units, assumptions, boundary conditions, validity range, and measurable quantities.
8. Write the paper in the required structure, preserving citation placeholders for unverified sources rather than inventing references.
9. Run a peer-review-style check and revise major gaps before finalizing.
10. When the user wants deliverables, keep the Markdown source and call `geomine-paper-pdf-export-skill` to produce a formula-safe PDF.

## Required Paper Sections

Academic paper outputs should include:

1. Title.
2. Abstract.
3. Keywords.
4. Introduction.
5. Research Questions and Hypotheses.
6. Literature Review.
7. Theoretical Framework or Methods / Model Formulation.
8. Mechanistic Analysis or Results.
9. Discussion.
10. Limitations.
11. Conclusion.
12. References.
13. Appendix: Symbols and Units, when equations are used.

## Quality Rules

- Do not produce unsupported industrial feasibility claims. Hydrogen production, energy efficiency, mining feasibility, or nuclear-facility claims require explicit system boundaries and energy/cost/safety constraints.
- Do not invent references, DOI values, datasets, experiments, sample counts, geologic observations, or model outputs.
- Mark weak claims as `requires further evidence` or `hypothesis only`.
- If the topic mentions G-value, radiolysis, electron, radical, or porous media, compare bulk water with porous/confined water.
- If the topic mentions nuclear radiation, hydrogen, radionuclide migration, or nuclear facilities, include safety and regulatory boundaries.
- Use cautious academic language unless the evidence is strong.
- Ensure conclusions include boundary conditions and are traceable to the evidence matrix.
