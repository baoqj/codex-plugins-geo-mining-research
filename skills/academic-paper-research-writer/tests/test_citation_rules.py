import re
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
DOI_PATTERN = re.compile(r"\b10\.\d{4,9}/\S+", re.IGNORECASE)


def test_citation_prompt_bans_fabricated_sources():
    text = (SKILL_ROOT / "prompts" / "citation_style.md").read_text(encoding="utf-8")
    assert "Do not invent" in text
    assert "DOI" in text
    assert "Citation needed" in text


def test_examples_do_not_assert_unverified_dois():
    for path in (SKILL_ROOT / "examples").glob("*.md"):
        text = path.read_text(encoding="utf-8")
        assert DOI_PATTERN.search(text) is None, path.name
        assert "Reference placeholder" in text or "Source to verify" in text
