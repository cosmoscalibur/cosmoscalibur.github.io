# /// script
# requires-python = ">=3.12"
# ///
"""Deterministic slug generation from a Spanish title, per CONTRIBUTING.md.

Character normalization only — never removes words. Lowercase, strip
diacritics (NFKD, drop combining marks), strip punctuation, collapse
whitespace into hyphens.
"""
import re
import sys
import unicodedata


def slugify(title: str) -> str:
    normalized = unicodedata.normalize("NFKD", title)
    without_diacritics = "".join(
        ch for ch in normalized if not unicodedata.combining(ch)
    )
    lowered = without_diacritics.lower()
    without_punctuation = re.sub(r"[^\w\s-]", "", lowered, flags=re.UNICODE)
    return re.sub(r"[-\s]+", "-", without_punctuation)


print(slugify(sys.argv[1]))
