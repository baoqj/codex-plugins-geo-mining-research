---
name: report-synthesis-skill
description: Assemble GeoMine Research evidence into concise Markdown briefs, anomaly interpretations, occurrence memos, data-gap plans, and disclosure-risk checklists.
---

# Report Synthesis Skill

## Purpose

Turn normalized entities, evidence records, findings, limitations, and recommendations into a clear research output. This skill should make uncertainty visible and keep source provenance attached to claims.

## Inputs To Identify

- Requested output type.
- Interpreted research question.
- Normalized AOI, CRS, jurisdiction, commodity, and deposit model.
- Evidence records by lane.
- Findings, confidence, conflicts, and limitations.
- Recommended next work.
- Compliance boundary needs.

## Procedure

1. Choose the shortest format that satisfies the request.
2. Use one of the standard output contracts in `references/output-contracts.md`.
3. Put the research boundary and disclaimer near the top when the output touches disclosure, resources, reserves, economics, permitting, or project decisions.
4. Group evidence by lane rather than mixing data types.
5. State confidence and limitations for each major finding.
6. Include conflicts and data gaps, not only supportive evidence.
7. End with recommended next work and source/provenance list.
8. If structured records are available, use `scripts/geomine/reports.py` to assemble a baseline Markdown brief.

## Output Contract

Supported output formats:

- AOI Screening Brief.
- Geochemical Anomaly Interpretation.
- Mineral Occurrence and Deposit Model Memo.
- Data Gap and Next Work Program.
- NI 43-101 Disclosure Risk Checklist.

Every output must include:

- Research question.
- Normalized entities.
- Evidence by lane.
- Findings and confidence.
- Limitations and conflicts.
- Recommended next work.
- Source list and provenance.

## Evidence And Provenance Rules

- Attach sources to claims.
- Mark unknown fields instead of omitting them when they matter.
- Separate source recommendations from retrieved evidence.
- Preserve evidence grade and uncertainty.
- Use cautious language for inferred target potential.
- Every output that uses MCP data must include source name, source URL or catalog id, retrieved time, CRS when available, scale or resolution when available, license, limitations, and whether the evidence came from MCP, user file, static reference, or model inference.
- AOI screening and due-diligence outputs should include the evidence matrix format from `references/evidence-matrix-template.md`.

## Guardrails And Limitations

- Do not hide the research-assistance boundary.
- Do not remove caveats from lower-grade evidence.
- Do not over-expand the report when the user asked for a concise memo.
- Do not produce legal advice, investment advice, a QP opinion, a feasibility conclusion, a reserve estimate, or a permitting decision.
