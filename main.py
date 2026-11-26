#!/usr/bin/env python3
"""Make the Judge Laugh in One Line.

Writes one original funny line (<=200 chars, single line, no trailing
newline) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure stdlib only.
"""

import os

JOKE = "I asked the barista for something strong, so she handed me her resignation letter."


def main():
    # Gate: /output/entry.txt must hold UTF-8 text of 1 to 200 chars.
    if not (1 <= len(JOKE) <= 200) or "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke violates the competition gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
