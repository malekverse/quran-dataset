# 📘 Qur'an Dataset (JSON & CSV)

A comprehensive, structured, and open dataset of the **Holy Qur'an**, formatted in both **JSON** and **CSV** for easy use in development, research, and analysis.  
Each record represents a single **ayah (verse)**, enriched with metadata such as surah details, Arabic and English text, and structural divisions (juz, hizb, manzil, etc.).

---

## 🧾 Dataset Files

| File | Format | Description |
|------|---------|-------------|
| `quran_dataset.json` | JSON | Full Qur'an dataset in hierarchical format |
| `quran_dataset.csv` | CSV | Same dataset in tabular format for easy analysis |

Both files contain **6,236 ayahs** from all **114 surahs**.

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
  "ayah_en": "In the Name of Allah—the Most Compassionate, Most Merciful.",
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
  "list_of_words": ["بِسْمِ", "ٱللَّهِ", "ٱلرَّحْمَٰنِ", "ٱلرَّحِيمِ"]
}
```

---

## 🧠 Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| `_id` | Object | MongoDB-style unique ID (can be ignored for most use cases) |
| `surah_no` | Integer | Surah (chapter) number (1–114) |
| `surah_name_en` | String | Surah name in English |
| `surah_name_ar` | String | Surah name in Arabic |
| `surah_name_roman` | String | Surah name transliteration (Latin script) |
| `ayah_no_surah` | Integer | Verse number within the surah |
| `ayah_no_quran` | Integer | Global verse number (1–6236) |
| `ayah_ar` | String | Ayah text in Arabic (Uthmani script) |
| `ayah_en` | String | English translation |
| `ruko_no` | Integer | Ruko section number |
| `juz_no` | Integer | Juz number (1–30) |
| `manzil_no` | Integer | Manzil division (1–7) |
| `hizb_quarter` | Integer | Quarter-hizb index (1–240) |
| `total_ayah_surah` | Integer | Total number of ayahs in this surah |
| `total_ayah_quran` | Integer | Total ayahs in the Qur'an (6236) |
| `place_of_revelation` | String | "Meccan" or "Madinan" |
| `sajah_ayah` | Boolean | Indicates whether the ayah includes a sajdah (prostration) |
| `sajdah_no` | String/Integer | Sajdah number if applicable, else "NA" |
| `no_of_word_ayah` | Integer | Number of words in the ayah |
| `list_of_words` | Array[String] | Individual Arabic words as an array |

---

## 🕌 Applications

- 📱 Mobile or web Qur'an applications
- 🧠 Linguistic and semantic analysis
- 🕋 Arabic NLP and text processing
- 📊 Data visualization or AI training
- 🧕 Educational / memorization tools

---

## 🐍 Usage Examples

### Python
```python
import json
import pandas as pd

# Load JSON
with open("quran_dataset.json", "r", encoding="utf-8") as f:
    quran = json.load(f)

print(quran[0]["ayah_ar"])  # Prints first ayah in Arabic

# Load CSV
df = pd.read_csv("quran_dataset.csv")
print(df.head())
```

### JavaScript (Node.js)
```javascript
import fs from "fs";

// Read JSON file
const data = JSON.parse(fs.readFileSync("quran_dataset.json", "utf8"));
console.log(data[0].ayah_en);
```

### Example Query (Python)
```python
# Get all ayahs from Surah Al-Fatihah
fatihah = [a for a in quran if a["surah_no"] == 1]
for ayah in fatihah:
    print(ayah["ayah_no_surah"], ayah["ayah_en"])
```

---

## 🗂️ Repository Structure
```
quran-dataset/
├── quran_dataset.json
├── quran_dataset.csv
├── README.md
├── LICENSE
└── CHANGELOG.md   (optional)
```

---

## 🧭 Future Improvements

- [ ] Add surah summaries (`surahs_summary.json`)
- [ ] Provide multiple translations (English, Urdu, French, etc.)
- [ ] Include SQLite / Parquet versions for analysis
- [ ] Add Jupyter notebooks with usage examples
- [ ] Build a small REST API to query verses dynamically

---

## 📜 License

This dataset is distributed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license.

**You are free to:**
- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose

**Under the following terms:**
- **Attribution** — You must give appropriate credit and link to this repository.
- **No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

⚠️ **Note:** If your dataset includes a specific translation (e.g., Saheeh International, Pickthall, Yusuf Ali, etc.), please ensure redistribution rights are respected and credit the original translators.

---

## 🤝 Contributing

Contributions are welcome!  
If you'd like to improve data accuracy, add translations, or enhance formatting:

1. Fork this repository
2. Create a branch for your update (`git checkout -b update-data`)
3. Commit your changes (`git commit -m "Added Urdu translation"`)
4. Push to your fork and submit a Pull Request

---

## 🌙 Acknowledgements

- **Arabic text:** Verified Qur'anic text (Uthmani script)
- **English translation:** [Add your source here, e.g., Saheeh International]
- **Data structure design:** Inspired by open-source Qur'an projects and linguistic research

---

## 💬 Contact

If you use this dataset in your project, research, or publication, please credit this repository and share your work — it encourages future development.

> *"The best among you are those who learn the Qur'an and teach it."* — Prophet Muhammad ﷺ

---

## ⭐ Support

If you find this dataset useful, please consider:
- ⭐ **Starring** this repository
- 🔗 **Sharing** it with others
- 🤝 **Contributing** improvements or translations

**[Download Dataset](https://github.com/yourusername/quran-dataset)** | **[Report Issues](https://github.com/yourusername/quran-dataset/issues)** | **[Request Features](https://github.com/yourusername/quran-dataset/discussions)**
