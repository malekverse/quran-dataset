# Changelog

## 1.1 (2026-10-04)

Corrected release. The record schema is unchanged, so existing code keeps working.

### Fixed
- Removed the duplicated second copy of the dataset: 12,472 records → 6,236 (reported in #1).
- 95:1 and 97:1: removed the Basmala that had been prefixed to the ayah text.
- 114:6: `list_of_words` and `no_of_word_ayah` contained the words of 114:5 (reported in #2).
- `list_of_words` / `no_of_word_ayah` rebuilt for every ayah. Pause and section marks (ۚ ۖ ۗ ۙ ۛ ۘ ۜ ۞ ۩) are no longer counted as words. 2,719 ayahs affected; total is now 77,430 words.
- 5:103: English translation was a copy of 5:102. Replaced with the translation of 5:103.
- 15:49: `hizb_quarter` 105 → 106.
- Surah 114 `surah_name_en`: "The Mankind" → "Mankind".
- Collapsed double spaces in 131 English ayahs.

### Added
- `scripts/validate.py`: integrity checks to run before every release.
- README: sources and credits, licensing clarification, conventions (Basmala, sajdah, ruku, spelling variants), verification method.

### Verified
- Arabic text and juz / manzil / hizb quarter / surah metadata cross-checked verse by verse against the Quran.com (Quran Foundation) API.

## 1.0

Initial release.
