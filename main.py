#!/usr/bin/env python3
"""Invent a Word We Need — make.fun entry.

Writes one invented English word with a one-line definition to
/output/entry.txt. The program is deterministic, uses only the
standard library, touches no network, and reads nothing outside
this repository.
"""

import os

ENTRY = "thresholdnesia (n.) — walking through a doorway and forgetting why you went there."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
