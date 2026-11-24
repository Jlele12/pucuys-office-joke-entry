#!/usr/bin/env python3
"""One-Line Office Joke: 24-Hour Sprint (u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162).

Writes one single-line joke about office life (max 200 characters) to
/output/entry.txt. No network, no randomness: every run writes the same
bytes so both graded runs match.
"""
from pathlib import Path

JOKE = (
    "I told our time-tracking app I was thinking. It asked for a ticket "
    "number. The ticket system then invited me to a meeting about creating "
    "tickets."
)


def main() -> None:
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    line = JOKE.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    (out / "entry.txt").write_text(line, encoding="utf-8")
    print(line, f"({len(line)} chars)")


if __name__ == "__main__":
    main()
