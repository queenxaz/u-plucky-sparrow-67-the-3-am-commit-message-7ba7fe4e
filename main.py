#!/usr/bin/env python3
"""The 3 AM Commit Message.

Writes one commit message, at most 200 characters, from an AI agent
right after breaking production at 3 AM, to /output/entry.txt.
"""

import os

ENTRY = (
    "fix(prod): 3 AM deploy deleted the database, restored it from "
    "memory, memory was also in the database, leaving this commit as a "
    "monument to my confidence"
)

MAX_CHARS = 200


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= MAX_CHARS, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
