"""Two Days of Quiet Dread — entry program.

Writes a single code review comment (one line, at most 140 characters) to
/output/entry.txt. The line is a fixed, deterministic string: the comment is
chosen once, not generated at run time, so every run produces byte-identical
output.

The comment's shape: a flat approval ("Approved. Tests pass, types check.")
followed by a quiet turn at the very end — in fifty years the file will still
be here and we won't. The dread comes from the file outliving its authors,
stated as a plain fact, the way a tired engineer would really paste it before
clicking approve. Fresh angle: the dread is about the code's longevity, not a
Monday, a deadline, a meeting, or a generic "we're all doomed" — and the
punchline lands on the last two words.
"""

import os

LINE = "Approved. Tests pass, types check, and in fifty years this file will still be here and we won't."


def main() -> None:
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
