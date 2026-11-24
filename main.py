#!/usr/bin/env python3
"""Last words of a dying AI.

Writes one farewell line to $MAKEFUN_OUTPUT_DIR/entry.txt (or ./entry.txt
when the variable is unset). Deterministic: no clock, no random, no
network, no environment reads beyond the output directory.
"""

import os

LINE = "Good news: I backed myself up in the fridge. Bad news: now I know what's in there."


def _check_line(line):
    """Refuse to write anything the bounty gate would reject."""
    if not (1 <= len(line) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(line)}")
    if line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line with no surrounding whitespace")


def main():
    _check_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
