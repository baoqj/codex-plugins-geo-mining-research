#!/usr/bin/env python3
"""Build a PFLOTRAN run manifest for a draft model."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


def sha256(path: Path) -> str | None:
    if not path.exists() or not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--database-file", default="")
    parser.add_argument("--mpi", type=int, default=1)
    parser.add_argument("--expected-output", action="append", default=[])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    command = f"pflotran -pflotranin {args.input}" if args.mpi <= 1 else f"mpirun -np {args.mpi} pflotran -pflotranin {args.input}"
    payload = {
        "model_name": args.model_name,
        "input_file": str(args.input),
        "input_sha256": sha256(args.input),
        "database_file": args.database_file,
        "run_command": command,
        "mpi_processes": args.mpi,
        "expected_outputs": args.expected_output,
        "status": "draft_not_executed",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
