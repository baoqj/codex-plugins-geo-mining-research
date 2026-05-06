"""Markdown report assembly for GeoMine Research."""

from __future__ import annotations

from .evidence_schema import EvidenceRecord, Finding, NormalizedAOI, Recommendation


DISCLAIMER = (
    "This output is for research assistance only. It is not legal advice, "
    "investment advice, a Qualified Person opinion, a feasibility study, a "
    "reserve estimate, or a permitting decision. All material technical "
    "disclosure should be reviewed by a Qualified Person and, where relevant, "
    "legal and regulatory counsel."
)


def assemble_research_brief(
    title: str,
    aoi: NormalizedAOI | None = None,
    evidence: list[EvidenceRecord] | None = None,
    findings: list[Finding] | None = None,
    recommendations: list[Recommendation] | None = None,
    limitations: list[str] | None = None,
) -> str:
    """Assemble a concise Markdown brief from structured records."""

    lines = [f"# {title}", "", "## Research Boundary", DISCLAIMER, ""]
    if aoi:
        lines.extend(
            [
                "## Normalized AOI",
                f"- Name: {aoi.name or 'Not supplied'}",
                f"- Province/Territory: {aoi.province_or_territory or 'Not supplied'}",
                f"- Country: {aoi.country}",
                f"- CRS: {aoi.crs or 'Not supplied'}",
                f"- NTS sheet: {aoi.nts_sheet or 'Not supplied'}",
                f"- Coordinates: {aoi.coordinates if aoi.coordinates is not None else 'Not supplied'}",
                "",
            ]
        )
        if aoi.assumptions:
            lines.append("### AOI Assumptions")
            lines.extend(f"- {item}" for item in aoi.assumptions)
            lines.append("")
        if aoi.warnings:
            lines.append("### AOI Warnings")
            lines.extend(f"- {item}" for item in aoi.warnings)
            lines.append("")

    if evidence:
        lines.append("## Evidence")
        for item in evidence:
            lines.append(item.to_markdown())
        lines.append("")

    if findings:
        lines.append("## Findings")
        for finding in findings:
            lines.append(
                f"- **{finding.title}** ({finding.confidence}, grade {finding.evidence_grade}): {finding.body}"
            )
            if finding.limitations:
                lines.append(f"  - Limitation: {finding.limitations}")
        lines.append("")

    if recommendations:
        lines.append("## Recommended Next Work")
        for recommendation in recommendations:
            lines.append(f"- **{recommendation.priority.title()}**: {recommendation.action}")
            lines.append(f"  - Rationale: {recommendation.rationale}")
            if recommendation.evidence_needed:
                lines.append(f"  - Evidence needed: {', '.join(recommendation.evidence_needed)}")
        lines.append("")

    if limitations:
        lines.append("## Limitations")
        lines.extend(f"- {item}" for item in limitations)
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"
