#!/usr/bin/env python3
"""Create a reproducible PHREEQC run manifest for local files."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path


def _sha256(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _file_record(path: Path) -> dict[str, object]:
    return {
        "path": str(path),
        "exists": path.exists(),
        "sha256": _sha256(path),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--objective", required=True)
    parser.add_argument("--model-type", required=True)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--database", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--selected-output", type=Path)
    parser.add_argument("--phreeqc", default=None, help="PHREEQC executable path; defaults to PATH lookup")
    parser.add_argument("--manifest", type=Path, help="Output manifest JSON path")
    args = parser.parse_args()

    phreeqc_path = args.phreeqc or shutil.which("phreeqc") or str(Path.home() / ".local" / "bin" / "phreeqc")
    manifest = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "objective": args.objective,
        "model_type": args.model_type,
        "phreeqc_executable": phreeqc_path,
        "command": [phreeqc_path, str(args.input), str(args.output), str(args.database)],
        "files": {
            "input": _file_record(args.input),
            "database": _file_record(args.database),
            "output": _file_record(args.output),
            "selected_output": _file_record(args.selected_output) if args.selected_output else None,
        },
        "status": "planned" if not args.output.exists() else "output_exists",
        "notes": [
            "Manifest records file paths and hashes only.",
            "Scientific validity requires independent review of data, database choice, and model assumptions.",
        ],
    }
    text = json.dumps(manifest, indent=2, ensure_ascii=False)
    if args.manifest:
        args.manifest.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
