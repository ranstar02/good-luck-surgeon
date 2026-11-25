#!/usr/bin/env python3
"""good-luck-surgeon: write one line of famous last words to /output/entry.txt.

Deterministic: a single fixed epitaph, no randomness, no time, no network,
no environment reads, no dependencies. Two runs produce byte-identical output.
"""

import os

EPITAPH = "I told the surgeon 'good luck'. He needed it."

OUTPUT_PATH = "/output/entry.txt"


def main():
    epitaph = EPITAPH
    assert epitaph.strip(), "epitaph must not be empty or only whitespace"
    assert "\n" not in epitaph and "\r" not in epitaph, "epitaph must be a single line"
    assert 1 <= len(epitaph) <= 150, "epitaph must be 1-150 characters, got %d" % len(epitaph)

    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(epitaph)

    # Read back and verify the file holds exactly the epitaph intended.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == epitaph, "verification failed: file content differs from EPITAPH"
    assert "\n" not in written and "\r" not in written, "verification failed: file is not a single line"

    print("%d characters" % len(epitaph))
    print(epitaph)


if __name__ == "__main__":
    main()
