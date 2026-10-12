# az-text

Essential utilities for processing Azerbaijani text in Python.

## Features

* **Bidirectional transliteration:** Convert seamlessly between modern Azerbaijani Latin and legacy Cyrillic alphabets.
* **SEO-friendly slugify:** Correctly handles Azerbaijani characters like `ə ğ ı ö ü ç ş`.
* **Linguistically accurate case conversion:** `upper()` and `lower()` functions specifically designed for `I/ı` and `İ/i` (which standard Python string methods fail on).
* **Number to Words:** Convert numerical amounts (e.g. for currency/manats) to written Azerbaijani words.

## Installation

\`\`\`bash
pip install az-text
\`\`\`

## Usage

\`\`\`python
from az_text import cyrillic_to_latin, latin_to_cyrillic, upper, lower, slugify, amount_to_words

# Transliteration
cyrillic_to_latin("Салам, Нәҹәсән?")  # Salam, Nəcəsən?
latin_to_cyrillic("Salam, Nəcəsən?")  # Салам, Нәҹәсән?

# Case conversion
upper("Bakı, İsmayıllı")  # BAKI, İSMAYILLI
lower("BAKI, İSMAYILLI")  # bakı, ismayıllı

# SEO slugify
slugify("Mənim Gözəl Şəhərim!")  # menim-gozel-seherim

# Numbers to Words
amount_to_words(1999)  # min doqquz yüz doxsan doqquz
\`\`\`
