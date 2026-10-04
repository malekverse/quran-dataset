# 📘 Qur'an Dataset (JSON & CSV)

A structured dataset of the **Holy Qur'an** in **JSON** and **CSV**, for development, research and analysis.
Each record is one **ayah (verse)** with its Arabic text (Uthmani script, Hafs 'an 'Asim), the public-domain English translation by Marmaduke Pickthall, and structural metadata (juz, hizb quarter, manzil, ruku, sajdah).

> **Version 1.2 (2026-10-04): corrected release.** Version 1.0 contained every ayah twice and several data errors.
> All of them are fixed and the dataset is now checked automatically. See [Corrections](#-corrections-in-v11) and [CHANGELOG.md](CHANGELOG.md).
> Jazakum Allahu khayran to everyone who reported problems.

---

## 🧾 Dataset Files

| File | Format | Description |
|------|--------|-------------|
| `quran_dataset.json` | JSON | Array of 6,236 ayah records |
| `quran_dataset.csv` | CSV | The same 6,236 records, one row per ayah (UTF-8) |
| `scripts/validate.py` | Python | Integrity checks; run `python scripts/validate.py` |

Both files contain exactly **6,236 ayahs** from all **114 surahs** (77,430 words).

---

## 🧩 JSON Data Structure

Example record:
```json
{
  "_id": { "$oid": "6905bdba2f1b958afd5c9952" },
  "surah_no": 1,
  "surah_name_en": "The Opener",
  "surah_name_ar": "الفاتحة",
  "surah_name_roman": "Al-Fatihah",
  "ayah_no_surah": 1,
  "ayah_no_quran": 1,
  "ayah_ar": "بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ",
  "ayah_en": "In the name of Allah, the Beneficent, the Merciful.",
  "ruko_no": 1,
  "juz_no": 1,
  "manzil_no": 1,
  "hizb_quarter": 1,
  "total_ayah_surah": 7,
  "total_ayah_quran": 6236,
  "place_of_revelation": "Meccan",
  "sajah_ayah": false,
  "sajdah_no": "NA",
  "no_of_word_ayah": 4,
  "list_of_words": "[بِسْمِ,ٱللَّهِ,ٱلرَّحْمَٰنِ,ٱلرَّحِيمِ]"
}
```

---

## 🧠 Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `_id` | Object | MongoDB-style ID left over from the original export; safe to ignore |
| `surah_no` | Integer | Surah number (1–114) |
| `surah_name_en` | String | Surah name in English |
| `surah_name_ar` | String | Surah name in Arabic |
| `surah_name_roman` | String | Surah name in Latin transliteration |
| `ayah_no_surah` | Integer | Ayah number within the surah |
| `ayah_no_quran` | Integer | Ayah number across the whole Qur'an (1–6236) |
| `ayah_ar` | String | Arabic text, Uthmani script, including pause marks (e.g. ۚ ۖ ۗ) |
| `ayah_en` | String | English translation by Marmaduke Pickthall (1930, public domain), see [Sources](#-sources-and-credits) |
| `ruko_no` | Integer | Ruku number (1–556, Tanzil numbering) |
| `juz_no` | Integer | Juz number (1–30) |
| `manzil_no` | Integer | Manzil number (1–7) |
| `hizb_quarter` | Integer | Rub' al-hizb (quarter-hizb) number (1–240) |
| `total_ayah_surah` | Integer | Number of ayahs in the surah |
| `total_ayah_quran` | Integer | Number of ayahs in the Qur'an (always 6236) |
| `place_of_revelation` | String | `"Meccan"` or `"Medinan"` |
| `sajah_ayah` | Boolean | `true` if the ayah is a place of prostration (sajdah) |
| `sajdah_no` | Integer / String | Sajdah number (1–15) if applicable, otherwise `"NA"` |
| `no_of_word_ayah` | Integer | Number of words in the ayah. Pause and section marks (ۚ ۖ ۗ ۙ ۛ ۘ ۜ ۞ ۩) are not counted as words. |
| `list_of_words` | String | The ayah's words as a bracketed, comma-separated string, e.g. `"[بِسْمِ,ٱللَّهِ]"`. See the parsing example below. |

### Conventions worth knowing

- **Basmala.** The Basmala is ayah 1 of Al-Fatihah only. For every other surah it is not part of the ayah text, so display it separately if your app shows it above each surah (except At-Tawbah).
- **Sajdah.** 15 places of prostration are marked, following the Madinah Mushaf. This includes **22:77**, which some schools (e.g. the Hanafi school) do not count; filter it out if you follow the 14-sajdah view.
- **Ruku.** `ruko_no` follows the Tanzil numbering (556 rukus). Some printed Mushafs and sites use a slightly different division.
- **Spelling.** The Uthmani orthography follows the Tanzil edition. Other Uthmani encodings (e.g. Quran.com) write a few words differently, such as `بَعْدَمَا` / `بَعْدَ مَا` (2:181, 8:6, 13:37) and `يَٰصَىٰحِبَىِ` / `يَـٰصَـٰحِبَىِ` (12:39, 12:41), and may omit the small iqlab meem signs (ۢ ۭ). These are encoding variants, not textual differences.

---

## 🐍 Usage Examples

### Python
```python
import json
import pandas as pd

with open("quran_dataset.json", encoding="utf-8") as f:
    quran = json.load(f)

print(quran[0]["ayah_ar"])  # first ayah in Arabic

# list_of_words is stored as a string: turn it into a real list
words = quran[0]["list_of_words"].strip("[]").split(",")

df = pd.read_csv("quran_dataset.csv", encoding="utf-8")
print(df.head())
```

### JavaScript (Node.js)
```javascript
import fs from "fs";

const data = JSON.parse(fs.readFileSync("quran_dataset.json", "utf8"));
console.log(data[0].ayah_en);

const words = data[0].list_of_words.slice(1, -1).split(",");
```

### Example query (Python)
```python
# All ayahs of Surah Al-Fatihah
for ayah in (a for a in quran if a["surah_no"] == 1):
    print(ayah["ayah_no_surah"], ayah["ayah_en"])
```

---

## ✅ Verification

The data is checked in two ways:

1. **`scripts/validate.py`** (run it after any change): 6,236 unique ayahs in Mushaf order, correct ayah count for each of the 114 surahs, no Basmala prefixed to any ayah except 1:1, word lists and counts consistent with the Arabic text (77,430 words), no missing or copied translations, and CSV identical to JSON.
2. **Cross-check against Quran.com (Quran Foundation API) on 2026-10-04**, verse by verse:
   - Arabic text: identical for all 6,236 ayahs once encoding differences are normalised (tatweel, iqlab meem signs, hamza and small-yeh code points). The only remaining differences are the five spelling variants listed above.
   - `juz_no`, `manzil_no`, `hizb_quarter`, `total_ayah_surah`, `place_of_revelation`, `surah_name_ar`: identical for every ayah.
   - English: Pickthall's translation as published by Quran.com, aligned verse by verse (spot-checked at 1:1, 1:7, 2:255, 112:1, 114:6).

If you find a problem, please [open an issue](https://github.com/malekverse/quran-dataset/issues) with the surah and ayah number.

---

## 🛠 Corrections in v1.1

| Problem in v1.0 | Fix |
|---|---|
| The whole dataset was included **twice** (12,472 records instead of 6,236) | Duplicate copy removed |
| **95:1** and **97:1** began with the Basmala (written `بِّسْمِ`), which is not part of these ayahs | Basmala removed from both ayahs |
| **114:6** had the word list and word count of 114:5 | Rebuilt from the ayah text |
| Word lists and counts treated pause marks (ۚ ۖ ۗ ۞ ۩ …) as words, in 2,719 ayahs | Rebuilt for all ayahs; pause marks are no longer counted |
| **5:103** English was a copy of 5:102 | Replaced with the correct translation of 5:103 |
| **15:49** `hizb_quarter` was 105 | Corrected to 106 (start of that quarter) |
| Surah 114 English name was "The Mankind" | "Mankind" |
| 131 English ayahs had double spaces | Whitespace normalised |
| *(v1.2)* English translation was the copyrighted *The Clear Quran* | Replaced with Pickthall's public-domain translation |

---

## 📚 Sources and credits

- **Arabic text:** Uthmani script, Hafs 'an 'Asim, in the orthography of the [Tanzil Project](https://tanzil.net). Tanzil's text may be copied and redistributed **verbatim** with a link back to tanzil.net; do not alter the Qur'anic text.
- **English translation:** *The Meaning of the Glorious Koran* by Mohammed Marmaduke Pickthall (1930), public domain. Text as published by [Quran.com](https://quran.com) (translation 19). Its archaic English ("ye", "Thou") is the translator's own and is kept verbatim. Versions 1.0–1.1 used *The Clear Quran* (© Dr. Mustafa Khattab), which was replaced in 1.2 because it is copyrighted.
- **Verification reference:** [Quran.com / Quran Foundation API](https://api-docs.quran.foundation).

## 📜 License

- The **structure, metadata and tooling** of this repository (field layout, numbering, scripts, documentation) are released under **CC BY 4.0**. Please credit and link this repository.
- The **Arabic Qur'anic text** keeps the Tanzil terms above (verbatim copies, with a link to tanzil.net). The **English translation** is in the public domain.

---

## 🤝 Contributing

Corrections and improvements are welcome:

1. Fork the repository and create a branch.
2. Make your change and run `python scripts/validate.py`. It must pass.
3. Open a Pull Request that names the affected surah and ayah numbers and the reference you used.

Changes to the Arabic text must be backed by a recognised Mushaf or by the Tanzil text.

---

## 🧭 Possible future improvements

- [ ] `list_of_words` as a real JSON array (in a new major version, to avoid breaking existing users)
- [ ] Additional translations with clear licensing
- [ ] Surah-level summary file
- [ ] SQLite / Parquet exports

---

> *"The best among you are those who learn the Qur'an and teach it."* (Sahih al-Bukhari 5027)

**[Download](https://github.com/malekverse/quran-dataset)** · **[Report an issue](https://github.com/malekverse/quran-dataset/issues)**
