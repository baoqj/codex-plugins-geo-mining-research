import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "skills" / "geomine-visualization-studio-skill" / "scripts" / "create_geomine_visualization.py"
SCENE = ROOT / "examples" / "visualization-uranium-basin-scene.json"


def test_visualization_scene_json_is_valid():
    data = json.loads(SCENE.read_text())
    assert data["title"] == "Athabasca Uranium Concept Model"
    assert data["status"] == "conceptual"
    assert data["layers"]
    assert data["structures"]
    assert data["provenance"]


def test_visualization_generator_creates_vite_project(tmp_path):
    out_dir = tmp_path / "demo"
    result = subprocess.run(
        [sys.executable, str(GENERATOR), "--scene-data", str(SCENE), "--output", str(out_dir)],
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert (out_dir / "package.json").exists()
    assert (out_dir / "src" / "App.tsx").exists()
    assert (out_dir / "src" / "scene-data.ts").exists()
    assert (out_dir / "src" / "vite-env.d.ts").exists()
    assert (out_dir / "scripts" / "verify.mjs").exists()

    package = json.loads((out_dir / "package.json").read_text())
    assert package["dependencies"]["three"]
    assert package["dependencies"]["@react-three/fiber"]
    assert "Athabasca Uranium Concept Model" in (out_dir / "src" / "scene-data.ts").read_text()
