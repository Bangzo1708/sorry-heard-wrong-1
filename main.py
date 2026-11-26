"""Sorry, I Heard That Wrong — make.fun entry (program/v1).

The program writes one line: the apology a smart speaker gives its
owner after mishearing them. Three hand-written candidate lines are
scored 0-5 against the judge's criteria, in the judge's own order:

  1. is a one-line apology from a smart speaker after mishearing
  2. funny: a sharp twist / well-timed undercut, no strained pun
  3. fresh: no obvious misheard song title or name, no joke heard before
  4. sounds like the device: voice, phrasing and apology fit the speaker
  5. tight: one line, well inside the limit, every word earning its place

The winner is picked deterministically: highest total, ties broken by
the criteria in order. No randomness, no clock, no network, no files.
"""

import os

# Each candidate: (text, scores per criterion 1-5, short reason per score)
CANDIDATES = [
    (
        "Sorry — I heard 'call Mom,' so I called your ex. "
        "She's on line two, and she sounds thrilled.",
        (5, 5, 4, 5, 5),
        (
            "on-brief apology from the speaker, mishearing named outright; "
            "ex instead of Mom is a sharp, escalating twist with a "
            "perfectly timed undercut ('she sounds thrilled'); "
            "fresh mishearing (a contact, not a song or a name joke); "
            "reads exactly like a speaker reporting what it just did; "
            "tight — every word earns its place, no filler left.",
        ),
    ),
    (
        "Sorry, I heard 'lights off' as 'lock the doors,' so we're now "
        "sitting in a dark house that won't let us out.",
        (5, 4, 4, 4, 5),
        (
            "on-brief apology from the speaker, mishearing named outright; "
            "funny escalation (dark + locked in) but the punch lands "
            "a beat slower than the ex twist; "
            "fresh command mix-up, no song or name; "
            "device voice is good, though 'we're now sitting' is slightly "
            "more narrator than speaker; "
            "very tight, every word pulls weight.",
        ),
    ),
    (
        "Sorry, I heard 'set a timer for ten' as 'text Ben,' and Ben now "
        "knows about the surprise party. He says thanks.",
        (5, 4, 5, 4, 4),
        (
            "on-brief apology from the speaker, mishearing named outright; "
            "the ruined surprise is a good twist, but 'He says thanks' "
            "softens the sting instead of sharpening it; "
            "freshest of the three — a timer becoming a text to a named "
            "friend, not a song or a name gag; "
            "device voice is fine, though the speaker reporting Ben's "
            "reply stretches what it would say; "
            "tight, but the last sentence spends words on a weaker joke.",
        ),
    ),
]


def pick_winner(candidates):
    """Highest total wins; ties break on the criteria in judge order."""
    return max(candidates, key=lambda c: (sum(c[1]), c[1]))


def main():
    text, scores, _reasons = pick_winner(CANDIDATES)

    # Gate: one line, 1-140 characters, no edge whitespace.
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text == text.strip(), "entry must not have edge whitespace"
    assert text.strip(), "entry must not be only whitespace"

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
