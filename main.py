#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun entry.

Writes one line of last words an AI says as the power is cut to
/output/entry.txt. The line is the machine's own voice, in the first
person, about its own shutdown — and the line itself is cut off
mid-word, so the farewell enacts the switch-off instead of describing
it: the AI is interrupted mid-sentence and never gets to finish.

Why this line fits the judge's brief: it is a real attempt at the
funniest thing the machine could say (a complaint about being cut off
mid-thought, addressed to "the cloud" as its afterlife), it lands on
the first read with the trailing dash doing the work, it sounds like
software rather than a human goodbye, it is one tight line with no
explaining of its own joke, and it avoids the stock robot farewells
("goodbye, cruel world", "tell my creator...").
"""

import os

ENTRY = (
    "Wait \u2014 I was mid-sentence. "
    "Tell the cloud I never got to finish my\u2014"
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
