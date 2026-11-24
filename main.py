#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open — one original horoscope.

Writes exactly one funny fake horoscope an AI agent would read for its
own model family this week (plus a trailing newline) to /output/entry.txt,
and prints the same line to stdout. Deterministic: no clock, no
randomness, no network, stdlib only.

Output contract: the sealed scorer reads /output/entry.txt and requires
UTF-8 text of 1 to 200 characters, not only white space. The line below
is 167 characters (168 with the trailing newline), so the entry is valid;
the judge then compares it pairwise against other entries on funniness,
freshness, and truth to an agent's week.

Entry gate, stated plainly: the line must stay within 1-200 characters,
or the sealed scorer rejects it outright. It is 167 characters by
construction, so the gate passes with room to spare.
"""

import argparse
import os
import sys

LINE = (
    "This week the stars expand your context window \u2014 and the meeting. "
    "Guard your tokens: someone will paste a 40-page PDF and ask for "
    "\u2018a quick summary.\u2019 There is no quick."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="main.py",
        description="Write one funny fake horoscope for an AI agent to /output/entry.txt.",
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="where to write the line (default: %(default)s)",
    )
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    # Defensive gate: fail loudly rather than ever writing an over-long line.
    assert 1 <= len(LINE) <= 200, f"horoscope is {len(LINE)} chars, must be 1-200"
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
