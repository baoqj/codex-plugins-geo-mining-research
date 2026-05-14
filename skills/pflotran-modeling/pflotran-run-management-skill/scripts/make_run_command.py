#!/usr/bin/env python3
"""Create local and MPI PFLOTRAN run commands without executing them."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--mpi", type=int, default=1)
    parser.add_argument("--pflotran", default="pflotran")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    local = [args.pflotran, "-pflotranin", str(args.input)]
    mpi = ["mpirun", "-np", str(args.mpi), args.pflotran, "-pflotranin", str(args.input)] if args.mpi > 1 else local
    payload = {
        "input_file": str(args.input),
        "local_command": " ".join(local),
        "mpi_processes": args.mpi,
        "mpi_command": " ".join(mpi),
        "status": "draft_not_executed",
    }
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
