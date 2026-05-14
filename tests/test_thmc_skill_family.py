import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_thmc_skill_family_validator_passes():
    result = subprocess.run(
        [sys.executable, "tests/validate_thmc_skill_family.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr

