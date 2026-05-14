---
name: ni43-101-disclosure-check-skill
description: Flag Canadian NI 43-101 and CIM terminology, evidence-gap, and disclosure-risk issues without providing legal advice or QP opinions.
---

# NI 43-101 Disclosure Check Skill

## Purpose

Review draft technical language, research briefs, or report summaries for terminology and evidence-risk flags related to Canadian mining disclosure. This skill identifies issues and safer wording directions only.

## Inputs To Identify

- Text to review and intended use.
- Jurisdiction and issuer or project context if supplied.
- Resource, reserve, exploration target, historical estimate, production, economics, metallurgy, permitting, Indigenous consultation, and environmental statements.
- Named Qualified Person or report source if supplied.
- Source documents and dates.

## Procedure

1. State that the review is not legal advice and not a Qualified Person opinion.
2. Identify CIM terminology: mineral resource, mineral reserve, inferred, indicated, measured, probable, proven, exploration target, and historical estimate.
3. Flag missing or unclear QP reliance.
4. Flag resource and reserve terminology misuse.
5. Flag historical estimate cautions that are missing or weak.
6. Flag unsupported economic language, such as guaranteed value, mineable, profitable, or reserve-like language without support.
7. Flag gaps in QA/QC, metallurgy, mining method, infrastructure, environmental baseline, permitting, Indigenous consultation, and data verification.
8. Suggest safer wording direction, not final legal text.
9. If the user asks for technical-report figures, disclosure caveat diagrams, evidence matrices, investor-facing visuals, or manuscript figure packages, route to `academic-figure-package-skill` and require QP/legal/investment caveats in captions.

## Output Contract

Return a concise Markdown checklist with:

- Risk level.
- Issue.
- Evidence or phrase reviewed.
- Why it matters.
- Safer wording direction.
- Required professional review.
- Overall limitations.
- Optional figure caveats for technical-report or investor-facing visuals.

## Evidence And Provenance Rules

- Quote only short snippets needed to identify the issue.
- Preserve report title, author, date, QP status, and issuer context when supplied.
- Distinguish between absent evidence and evidence not provided in the prompt.
- Identify where a Qualified Person, legal counsel, engineer, metallurgist, environmental consultant, or Indigenous consultation specialist should review.

## Guardrails And Limitations

- Do not provide legal advice.
- Do not provide or imply a QP opinion.
- Do not validate mineral resources or reserves.
- Do not state that disclosure complies with NI 43-101.
- Do not rewrite disclosure into final filing language.
- Do not soften serious missing-evidence risks.
