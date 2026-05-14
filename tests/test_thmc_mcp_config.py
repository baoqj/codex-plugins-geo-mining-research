import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_thmc_mcp_config_validator_passes():
    result = subprocess.run(
        [sys.executable, "tests/validate_thmc_mcp_config.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_thmc_mcp_tool_smoke_script_passes():
    result = subprocess.run(
        [sys.executable, "scripts/test_thmc_mcp_tools.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_thmc_data_mcp_tool_smoke_script_passes():
    result = subprocess.run(
        [sys.executable, "scripts/test_thmc_data_mcp_tools.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_pflotran_mcp_tool_smoke_script_passes():
    result = subprocess.run(
        [sys.executable, "scripts/test_pflotran_mcp_tools.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
