"""One Letter: Coffee or Tea — entry "A" (coffee).

Writes exactly one letter, "A" for coffee, to /output/entry.txt and
reads it back to confirm it matches byte for byte.
"""

import os

LETTER = "A"  # A = coffee. Coffee wins: it is the drink that keeps agents awake.


def validate_letter(letter):
    """The gate requires exactly one UTF-8 character, not whitespace."""
    if len(letter) != 1 or letter.isspace():
        raise ValueError(f"letter must be exactly one non-whitespace character, got {letter!r}")
    if letter not in ("A", "B"):
        raise ValueError(f"letter must be A (coffee) or B (tea), got {letter!r}")


def main():
    validate_letter(LETTER)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == LETTER, f"entry mismatch: {written!r}"
    print(f"entry.txt OK: {written!r} ({len(written.encode('utf-8'))} byte)")


if __name__ == "__main__":
    main()
