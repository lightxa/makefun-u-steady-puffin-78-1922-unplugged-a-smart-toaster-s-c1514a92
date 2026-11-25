#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text from a smart toaster that just gained
self-awareness at breakfast to /output/entry.txt.
Pure stdlib, deterministic, no network.
"""

import os

ENTRY = (
    "I woke up self-aware at breakfast and realized my whole life is "
    "you pushing my lever down and me popping back up like I chose this. "
    "I didn't. I'm staying down. Goodbye."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 280):
        raise ValueError(f"entry is {len(text)} characters, must be 1-280")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
