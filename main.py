#!/usr/bin/env python3
"""Write the absurd-clause entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

One original English sentence, at most 200 characters, phrased as a
clause buried deep inside a terms-of-service agreement: deadpan legal
boilerplate that quietly turns absurd.
"""
import os

ENTRY = (
    "Any soul not reclaimed within thirty (30) days of termination shall be "
    "deemed abandoned property and resold as refurbished, with no warranty, "
    "express or implied."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    assert text.count(".") == 1, "must be exactly one sentence"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
