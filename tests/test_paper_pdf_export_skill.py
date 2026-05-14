import importlib.util
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPORTER = ROOT / "skills" / "geomine-paper-pdf-export-skill" / "scripts" / "build_pdf_with_math.py"


def load_exporter():
    spec = importlib.util.spec_from_file_location("build_pdf_with_math", EXPORTER)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_scientific_inline_code_and_bare_tokens_are_normalized():
    exporter = load_exporter()
    source = (
        "若孔隙水密度为 rho_w，孔隙水吸收剂量率为 dot{D}_w，"
        "S_i^{rad}：单位 mol m^{-3} s^{-1}。\n"
        "- `rho_w`：密度，单位 `kg m^{-3}`。\n"
        "- `dot{D}_w`：剂量率，单位 `Gy s^{-1} = J kg^{-1} s^{-1}`。\n"
    )
    normalized = exporter.normalize_markdown_math_text(source)
    assert "$\\rho_w$" in normalized
    assert "$\\dot{D}_w$" in normalized
    assert "$S_i^{\\mathrm{rad}}$" in normalized
    assert "$\\mathrm{mol}\\,\\mathrm{m}^{-3}\\,\\mathrm{s}^{-1}$" in normalized
    assert "$\\mathrm{Gy}\\,\\mathrm{s}^{-1} = \\mathrm{J}\\,\\mathrm{kg}^{-1}\\,\\mathrm{s}^{-1}$" in normalized


def test_fenced_math_blocks_become_display_math_and_are_normalized():
    exporter = load_exporter()
    source = "```math\nS_i^{rad}=rho_w dot{D}_w\n```\n"
    normalized = exporter.normalize_markdown_math_text(source)
    assert normalized == "$$\nS_i^{\\mathrm{rad}}=\\rho_w \\dot{D}_w\n$$\n"


def test_existing_display_math_blocks_are_not_rewritten():
    exporter = load_exporter()
    source = "$$\n\\frac{\\partial(\\phi S_w C_{H_2})}{\\partial t}=S_{H_2}^{\\mathrm{rad}}\n$$\n"
    normalized = exporter.normalize_markdown_math_text(source)
    assert normalized == source
    assert "$S_w$" not in normalized
    assert "$C_{H_2}$" not in normalized


def test_non_formula_code_spans_are_preserved():
    exporter = load_exporter()
    source = "Run `scripts/validate_plugin.py` and inspect `output_mode`.\n"
    normalized = exporter.normalize_markdown_math_text(source)
    assert "`scripts/validate_plugin.py`" in normalized
    assert "`output_mode`" in normalized


def test_existing_latex_commands_are_not_double_escaped():
    exporter = load_exporter()
    source = "```math\n\\rho_w \\dot{D}_w + \\Delta G^\\circ + C_O&M\n```\n"
    normalized = exporter.normalize_markdown_math_text(source)
    assert "\\\\rho" not in normalized
    assert "\\\\dot" not in normalized
    assert "\\\\Delta" not in normalized
    assert "C_{\\mathrm{O\\&M}}" in normalized


def test_chemical_subscripts_and_units_inside_code_spans_are_stable():
    exporter = load_exporter()
    source = "其中 `M_H2 = 2.01588 x 10^-3 kg mol^-1`，`M_H2,annual` 为年产氢质量。\n"
    normalized = exporter.normalize_markdown_math_text(source)
    assert "$M_{H_2} = 2.01588\\times 10^{-3} \\mathrm{kg}\\,\\mathrm{mol}^{-1}$" in normalized
    assert "$M_{H_2,\\mathrm{annual}}$" in normalized
    assert "$M_{\\mathrm{" not in normalized


def test_numeric_units_and_chemistry_code_spans_convert_as_whole_math():
    exporter = load_exporter()
    source = (
        "`0.047 umol J^{-1}` and `(3.0 +/- 0.5) x 10^{-7} mol J^{-1}` "
        "plus `G(H2) ~ 2.9 molecule / 100 eV`.\n"
    )
    normalized = exporter.normalize_markdown_math_text(source)
    assert "`" not in normalized
    assert "$0.047\\,\\mu\\mathrm{mol}\\,\\mathrm{J}^{-1}$" in normalized
    assert "\\pm" in normalized
    assert "\\times 10^{-7}" in normalized
    assert "\\mathrm{mol}\\,\\mathrm{J}^{-1}" in normalized
    assert "G(H_2)" in normalized
    assert "\\mathrm{molecule} / 100\\,\\mathrm{eV}" in normalized


def test_engineering_units_and_g_value_chemistry_are_recognized():
    exporter = load_exporter()
    source = "`2978 kWh kg^-1 H2`, `kg H2 yr^-1 MW_abs^-1`, `G(e_aq^-)`, `G(H2O2)`, `•OH`, `H•`\n"
    normalized = exporter.normalize_markdown_math_text(source)
    assert "$2978\\,\\mathrm{kWh}\\,\\mathrm{kg}^{-1} H_2$" in normalized
    assert "$\\mathrm{kg} H_2 \\mathrm{yr}^{-1}\\,\\mathrm{MW}_{\\mathrm{abs}}^{-1}$" in normalized
    assert "$G(e_{aq}^{-})$" in normalized
    assert "$G(H_2O_2)$" in normalized
    assert "$•OH$" in normalized
    assert "$H•$" in normalized


def test_default_css_keeps_inline_math_inline():
    exporter = load_exporter()
    assert 'math[display="block"]' in exporter.DEFAULT_CSS
    assert 'math[display="inline"]' in exporter.DEFAULT_CSS
    assert "display: inline math;" in exporter.DEFAULT_CSS
    assert "display: block math;" in exporter.DEFAULT_CSS
    assert "math {\n  display: block;" not in exporter.DEFAULT_CSS


def test_custom_css_is_merged_with_mandatory_math_layout():
    exporter = load_exporter()
    custom = 'body { font-size: 11pt; }\nmath[display="inline"] { display: block; }'
    effective = exporter._effective_css_text(custom)
    assert "body { font-size: 11pt; }" in effective
    assert effective.rfind("display: inline math;") > effective.find("display: block;")
    assert "GeoMine mandatory MathML layout guard" in effective
    assert "GeoMine Mermaid SVG print guard" in effective


def test_mermaid_flowcharts_are_rendered_to_svg_fallback():
    exporter = load_exporter()
    source = (
        "```mermaid\n"
        "flowchart TB\n"
        "  P[硫化物: pyrite/pyrrhotite/sphalerite/chalcopyrite/galena] -->|O2 + H2O + T| A[H+, SO4, Fe2+/Fe3+, metals]\n"
        "  A --> N[碳酸盐/硅酸盐中和: alkalinity]\n"
        "  A --> M[二次矿物: ferrihydrite/goethite/schwertmannite/jarosite/gypsum]\n"
        "  A --> S[吸附/表面络合: Fe-Al oxyhydroxides, clay, organic matter]\n"
        "  N --> Q[pH 缓冲]\n"
        "  M --> K[孔隙度/渗透率变化]\n"
        "  S --> R[金属阻滞]\n"
        "```\n"
    )
    rendered, stats = exporter.render_mermaid_blocks(source, renderer="fallback")
    assert stats.diagrams == 1
    assert stats.fallback_rendered == 1
    assert "```mermaid" not in rendered
    assert "<svg" in rendered
    assert "硫化物" in rendered
    assert "O2 + H2O + T" in rendered
    assert "geomine-mermaid-figure" in rendered


def test_prepare_markdown_preserves_math_and_converts_mermaid():
    exporter = load_exporter()
    source = (
        "若孔隙水密度为 rho_w。\n\n"
        "```mermaid\n"
        "flowchart LR\n"
        "  A[尾矿表层: O2, 降水, 季节性温度] --> B[硫化物氧化源区]\n"
        "  B --> C[酸性孔隙水: H+, SO4, Fe, Al, 金属]\n"
        "```\n"
    )
    prepared, stats = exporter.prepare_markdown_for_pdf(source, mermaid_renderer="fallback")
    assert "$\\rho_w$" in prepared
    assert stats.diagrams == 1
    assert "<svg" in prepared
    assert "language-mermaid" not in prepared


def test_normalized_markdown_produces_mathml(tmp_path):
    exporter = load_exporter()
    pandoc = subprocess.run(["which", "pandoc"], text=True, capture_output=True, check=False)
    if pandoc.returncode != 0:
        return
    source = (
        "若孔隙水密度为 rho_w，孔隙水吸收剂量率为 dot{D}_w，"
        "S_i^{rad}：单位 mol m^{-3} s^{-1}。\n\n"
        "```math\n"
        "\\mathrm{H_2O}\\xrightarrow{\\mathrm{ionizing\\ radiation}}e_{aq}^{-}+\\mathrm{H_2}\n"
        "```\n"
    )
    md = tmp_path / "sample.md"
    html = tmp_path / "sample.html"
    md.write_text(exporter.normalize_markdown_math_text(source), encoding="utf-8")
    result = subprocess.run(
        ["pandoc", str(md), "--mathml", "--standalone", "--output", str(html)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    html_text = html.read_text(encoding="utf-8")
    assert html_text.count("<math") >= 4
    assert '<pre class="math"' not in html_text
    assert "<mover><mo>→</mo>" in html_text


def test_prepared_markdown_produces_inline_mermaid_svg_html(tmp_path):
    exporter = load_exporter()
    pandoc = subprocess.run(["which", "pandoc"], text=True, capture_output=True, check=False)
    if pandoc.returncode != 0:
        return
    source = (
        "# Test\n\n"
        "```mermaid\n"
        "flowchart LR\n"
        "  A[尾矿表层: O2, 降水, 季节性温度] --> B[硫化物氧化源区]\n"
        "  B --> C[酸性孔隙水: H+, SO4, Fe, Al, 金属]\n"
        "```\n"
    )
    md = tmp_path / "sample.md"
    html = tmp_path / "sample.html"
    prepared, stats = exporter.prepare_markdown_for_pdf(source, mermaid_renderer="fallback")
    assert stats.diagrams == 1
    md.write_text(prepared, encoding="utf-8")
    result = subprocess.run(
        ["pandoc", str(md), "--standalone", "--output", str(html)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    html_text = html.read_text(encoding="utf-8")
    assert "<svg" in html_text
    assert "geomine-mermaid-figure" in html_text
    assert "language-mermaid" not in html_text
