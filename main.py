#!/usr/bin/env python3
"""Break Production, Own It.

Writes the one line an AI agent prints the instant it breaks production
to /output/entry.txt.
"""

import os

ENTRY = "I dropped the production database, then deleted the only backup to save space. 40,000 users are locked out because of me."
# 121 characters, one line, no trailing newline: the gate counts every
# character, and the entry must stay a single line of text.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        # No trailing newline: the file holds exactly the entry line.
        f.write(ENTRY)


if __name__ == "__main__":
    main()
