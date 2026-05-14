from pathlib import Path


EXAMPLE_ROOT = Path(__file__).resolve().parents[1] / "examples"


REQUIRED_HEADINGS = [
    "## Abstract",
    "## Keywords",
    "## Introduction",
    "## Research Questions and Hypotheses",
    "## Literature Review",
    "## Discussion",
    "## Limitations",
    "## Conclusion",
    "## References",
    "## Appendix: Symbols and Units",
]


def test_porous_media_example_has_publication_sections():
    text = (EXAMPLE_ROOT / "porous_media_radiolysis_paper.md").read_text(
        encoding="utf-8"
    )
    for heading in REQUIRED_HEADINGS:
        assert heading in text
    assert "bulk water" in text.lower()
    assert "porous media" in text.lower()
    assert "Safety and Regulatory Boundary" in text
    assert "hypothesis only" in text
    assert "requires further evidence" in text


def test_all_examples_have_core_academic_sections():
    for path in EXAMPLE_ROOT.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        for heading in [
            "## Abstract",
            "## Research Questions and Hypotheses",
            "## Evidence Matrix",
            "## Limitations",
            "## Conclusion",
            "## References",
        ]:
            assert heading in text, f"{path.name} missing {heading}"
