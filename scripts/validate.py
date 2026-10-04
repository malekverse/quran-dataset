"""Integrity checks for quran_dataset.json and quran_dataset.csv.

Run from the repository root:  python scripts/validate.py
Exits with code 1 if any check fails. Needs only the Python standard library.
"""
import csv
import json
import sys
import unicodedata
from collections import Counter

EXPECTED_AYAHS = 6236
EXPECTED_SURAHS = 114
EXPECTED_WORDS = 77430  # Tanzil Uthmani text, pause marks excluded

# Verses per surah (Hafs 'an 'Asim)
AYAHS_PER_SURAH = [
    7, 286, 200, 176, 120, 165, 206, 75, 129, 109, 123, 111, 43, 52, 99, 128, 111, 110, 98, 135,
    112, 78, 118, 64, 77, 227, 93, 88, 69, 60, 34, 30, 73, 54, 45, 83, 182, 88, 75, 85,
    54, 53, 89, 59, 37, 35, 38, 29, 18, 45, 60, 49, 62, 55, 78, 96, 29, 22, 24, 13,
    14, 11, 11, 18, 12, 12, 30, 52, 52, 44, 28, 28, 20, 56, 40, 31, 50, 40, 46, 42,
    29, 19, 36, 25, 22, 17, 19, 26, 30, 20, 15, 21, 11, 8, 8, 19, 5, 8, 8, 11,
    11, 8, 3, 9, 5, 4, 7, 3, 6, 3, 5, 4, 5, 6,
]


def is_word(token):
    """Pause and recitation marks (e.g. ۚ ۖ ۗ ۞ ۩) are tokens without letters, not words."""
    return any(unicodedata.category(ch).startswith("L") for ch in token)


def main():
    with open("quran_dataset.json", encoding="utf-8") as f:
        rows = json.load(f)
    with open("quran_dataset.csv", encoding="utf-8", newline="") as f:
        csv_rows = list(csv.DictReader(f))

    failures = []

    def check(ok, message):
        print(("PASS  " if ok else "FAIL  ") + message)
        if not ok:
            failures.append(message)

    check(len(rows) == EXPECTED_AYAHS, f"JSON has {EXPECTED_AYAHS} ayahs (found {len(rows)})")
    check(len(csv_rows) == EXPECTED_AYAHS, f"CSV has {EXPECTED_AYAHS} ayahs (found {len(csv_rows)})")

    keys = [(r["surah_no"], r["ayah_no_surah"]) for r in rows]
    check(len(set(keys)) == len(keys), "no duplicated (surah_no, ayah_no_surah)")
    check(keys == sorted(keys), "ayahs are in Mushaf order")
    check([r["ayah_no_quran"] for r in rows] == list(range(1, len(rows) + 1)), "ayah_no_quran runs 1..6236")

    per_surah = Counter(r["surah_no"] for r in rows)
    check(
        len(per_surah) == EXPECTED_SURAHS
        and all(per_surah[i + 1] == n for i, n in enumerate(AYAHS_PER_SURAH)),
        "every surah has its correct number of ayahs",
    )
    check(all(r["total_ayah_surah"] == AYAHS_PER_SURAH[r["surah_no"] - 1] for r in rows), "total_ayah_surah is correct")

    def skeleton(text):
        """Letters only: drops harakat and other combining marks, so diacritic order does not matter."""
        return "".join(ch for ch in text if not unicodedata.category(ch).startswith("M"))

    basmala = skeleton(rows[0]["ayah_ar"])  # 1:1
    embedded = [
        f"{r['surah_no']}:{r['ayah_no_surah']}"
        for r in rows[1:]
        if skeleton(r["ayah_ar"]).startswith(basmala)
    ]
    check(not embedded, f"Basmala is not prefixed to any verse other than 1:1 {embedded or ''}")

    words_ok = True
    for r in rows:
        words = [w for w in r["ayah_ar"].split() if is_word(w)]
        if r["list_of_words"] != "[" + ",".join(words) + "]" or r["no_of_word_ayah"] != len(words):
            words_ok = False
            print(f"      word list mismatch at {r['surah_no']}:{r['ayah_no_surah']}")
    check(words_ok, "list_of_words and no_of_word_ayah match ayah_ar")
    total_words = sum(r["no_of_word_ayah"] for r in rows)
    check(total_words == EXPECTED_WORDS, f"{EXPECTED_WORDS} words in total (found {total_words})")

    check(all(r["ayah_en"].strip() for r in rows), "every ayah has an English translation")
    # Pickthall translates 102:3 and 102:4 identically ("Nay, but ye will come to know!");
    # that is the translator's own wording, not a data error.
    same_wording_by_translator = {(102, 4)}
    copied = [
        f"{b['surah_no']}:{b['ayah_no_surah']}"
        for a, b in zip(rows, rows[1:])
        if a["ayah_en"] == b["ayah_en"]
        and a["ayah_ar"] != b["ayah_ar"]
        and (b["surah_no"], b["ayah_no_surah"]) not in same_wording_by_translator
    ]
    check(not copied, f"no translation copied from the previous ayah {copied or ''}")

    check(
        all(
            csv_rows[i]["ayah_ar"] == rows[i]["ayah_ar"]
            and csv_rows[i]["ayah_en"] == rows[i]["ayah_en"]
            and csv_rows[i]["list_of_words"] == rows[i]["list_of_words"]
            for i in range(min(len(rows), len(csv_rows)))
        ),
        "CSV and JSON contain the same text",
    )

    print()
    if failures:
        print(f"{len(failures)} check(s) failed.")
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
