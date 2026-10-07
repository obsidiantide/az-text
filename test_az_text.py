import pytest
from az_text import cyrillic_to_latin, upper, lower, slugify, amount_to_words

def test_cyrillic_to_latin():
    assert cyrillic_to_latin("Салам, Нәҹәсән?") == "Salam, Nəcəsən?"

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
