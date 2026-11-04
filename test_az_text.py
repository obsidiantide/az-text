import pytest
from az_text import cyrillic_to_latin, latin_to_cyrillic, upper, lower, slugify, amount_to_words

def test_cyrillic_to_latin():
    assert cyrillic_to_latin("Салам, Нәҹәсән?") == "Salam, Nəcəsən?"
    assert cyrillic_to_latin("Бакы, Ҝәнҹә, Нахчыван, Шәки") == "Bakı, Gəncə, Naxçıvan, Şəki"
    assert cyrillic_to_latin("Ғәләбә") == "Ğələbə"
    assert cyrillic_to_latin("Јазычы") == "Yazıçı"
    assert cyrillic_to_latin("Өмүр вә Үмид") == "Ömür və Ümid"

def test_latin_to_cyrillic():
    assert latin_to_cyrillic("Salam, Nəcəsən?") == "Салам, Нәҹәсән?"
    assert latin_to_cyrillic("Bakı, Gəncə, Naxçıvan, Şəki") == "Бакы, Ҝәнҹә, Нахчыван, Шәки"
    assert latin_to_cyrillic("Ğələbə") == "Ғәләбә"
    assert latin_to_cyrillic("Yazıçı") == "Јазычы"
    assert latin_to_cyrillic("Ömür və Ümid") == "Өмүр вә Үмид"

def test_transliteration_roundtrip():
    phrase = "Bakı, Gəncə, Naxçıvan, Şəki"
    assert cyrillic_to_latin(latin_to_cyrillic(phrase)) == phrase

def test_upper_lower():
    assert upper("Bakı, İsmayıllı") == "BAKI, İSMAYILLI"
    assert lower("BAKI, İSMAYILLI") == "bakı, ismayıllı"

def test_slugify():
    assert slugify("Mənim Gözəl Şəhərim!") == "menim-gozel-seherim"

def test_amount_to_words():
    assert amount_to_words(0) == "sıfır"
    assert amount_to_words(1) == "bir"
    assert amount_to_words(25) == "iyirmi beş"
    assert amount_to_words(100) == "yüz"
    assert amount_to_words(105) == "yüz beş"
    assert amount_to_words(1999) == "min doqquz yüz doxsan doqquz"
    assert amount_to_words(25000) == "iyirmi beş min"
    assert amount_to_words(1000000) == "bir milyon"
    assert amount_to_words(2500000) == "iki milyon beş yüz min"
    assert amount_to_words(1000000000) == "bir milyard"
    assert amount_to_words(3400000000) == "üç milyard dörd yüz milyon"

def test_amount_to_words_rejects_negative():
    with pytest.raises(ValueError):
        amount_to_words(-5)

@pytest.mark.parametrize("value", [1.5, "10", None, True])
def test_amount_to_words_rejects_non_integers(value):
    with pytest.raises(TypeError):
        amount_to_words(value)

def test_amount_to_words_thousand_boundaries():
    assert amount_to_words(1000) == "min"
    assert amount_to_words(2000) == "iki min"
    assert amount_to_words(1001000) == "bir milyon min"
    assert amount_to_words(999999) == "doqquz yüz doxsan doqquz min doqquz yüz doxsan doqquz"
