#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse.

Prints one original one-liner in which a robot vacuum explains why it
missed a spot, and writes the same line to /output/entry.txt for the
make.fun program/v1 grader. Standard library only, deterministic:
every run produces the same bytes. No file access depends on the
working directory.
"""

import os
from pathlib import Path

LINE = (
    "I didn't miss that spot \u2014 the dust bunny unionised, "
    "and I'm not allowed to cross a picket line."
)


def main() -> None:
    # The gate allows 1-120 characters; fail loudly instead of shipping
    # an invalid entry if the line is ever edited past the limit.
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} characters"
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
