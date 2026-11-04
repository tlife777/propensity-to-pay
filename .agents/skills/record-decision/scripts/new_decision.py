#!/usr/bin/env python3
"""Create docs/decisions/NNN-short-name.md with the next number and the AGENTS.md fields."""
import re
import sys
from pathlib import Path

# scripts/ -> record-decision/ -> skills/ -> .agents/ -> repository root
DECISIONS = Path(__file__).resolve().parents[4] / "docs" / "decisions"
SHORT_NAME = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
TEMPLATE = """# {number}:
Question:
Options:
Choice:
Why:
Evidence:
Decided by:
For the presentation:
"""


def next_number() -> int:
    numbers = [int(path.name[:3]) for path in DECISIONS.glob("[0-9][0-9][0-9]-*.md")]
    return max(numbers, default=0) + 1


def main() -> None:
    if len(sys.argv) != 2 or not SHORT_NAME.fullmatch(sys.argv[1]):
        sys.exit("Usage: new_decision.py short-name (lowercase letters, numbers and hyphens)")

    DECISIONS.mkdir(parents=True, exist_ok=True)
    number = f"{next_number():03d}"
    path = DECISIONS / f"{number}-{sys.argv[1]}.md"
    with path.open("x", encoding="utf-8", newline="\n") as file:
        file.write(TEMPLATE.format(number=number))
    print(path)


if __name__ == "__main__":
    main()
