from geomine.aoi import normalize_aoi
from geomine.evidence_schema import EvidenceRecord, Finding, Recommendation
from geomine.reports import assemble_research_brief


def test_evidence_record_serializes_and_renders():
    record = EvidenceRecord(
        source="BC MINFILE",
        title="Nearby Cu occurrence",
        evidence_type="mineral-occurrence",
        summary="Occurrence is relevant but location confidence needs review.",
        grade="b",
        jurisdiction="British Columbia",
    )
    assert record.as_dict()["grade"] == "B"
    assert "BC MINFILE" in record.to_markdown()


def test_aoi_warning_and_brief_rendering():
    aoi = normalize_aoi({"name": "Example AOI", "province": "Ontario"})
    assert aoi.country == "Canada"
    assert "CRS missing" in " ".join(aoi.warnings)
    brief = assemble_research_brief(
        "Example Brief",
        aoi=aoi,
        findings=[Finding("Data gap", "No coordinates supplied.", evidence_grade="D")],
        recommendations=[Recommendation("Resolve AOI geometry.", "Spatial checks need geometry.")],
    )
    assert "Example Brief" in brief
    assert "Qualified Person opinion" in brief
