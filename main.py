#!/usr/bin/env python3
"""Write the two-line make.fun entry."""

import os
import sys
from pathlib import Path

TEXT = "The cat has not moved since six.\nThe square of light has, and takes her with it."


def main() -> None:
    assert 1 <= len(TEXT) <= 280
    output_dir = Path(
        os.environ["MAKEFUN_OUTPUT_DIR"]
        if "MAKEFUN_OUTPUT_DIR" in os.environ
        else os.environ.get("OUTPUT_DIR", "/output")
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
