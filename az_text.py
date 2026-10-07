import re

CYRILLIC_TO_LATIN = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'Q', 'Д': 'D', 'Е': 'E', 'Ә': 'Ə', 'Ж': 'J',
    'З': 'Z', 'И': 'İ', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
    'Ө': 'Ö', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ү': 'Ü', 'Ф': 'F',
    'Х': 'X', 'Һ': 'H', 'Ц': 'Ts', 'Ч': 'Ç', 'Ш': 'Ş', 'Ы': 'I', 'Э': 'E',
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'q', 'д': 'd', 'е': 'e', 'ә': 'ə', 'ж': 'j',
    'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
    'ө': 'ö', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ү': 'ü', 'ф': 'f',
    'х': 'x', 'һ': 'h', 'ц': 'ts', 'ч': 'ç', 'ш': 'ş', 'ы': 'ı', 'э': 'e'
}

def cyrillic_to_latin(text: str) -> str:
    """Transliterator for Azerbaijani Cyrillic to Latin."""
    return ''.join(CYRILLIC_TO_LATIN.get(char, char) for char in text)

def upper(text: str) -> str:
    """Linguistically accurate uppercase for Azerbaijani."""
    text = text.replace('i', 'İ').replace('ı', 'I')
    return text.upper()

def lower(text: str) -> str:
    """Linguistically accurate lowercase for Azerbaijani."""
    text = text.replace('İ', 'i').replace('I', 'ı')
    return text.lower()

def slugify(text: str) -> str:
    """SEO-friendly slugify that correctly handles Azerbaijani characters."""
    replacements = {
        'ə': 'e', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ü': 'u', 'ç': 'c', 'ş': 's',
        'Ə': 'e', 'Ğ': 'g', 'İ': 'i', 'I': 'i', 'Ö': 'o', 'Ü': 'u', 'Ç': 'c', 'Ş': 's'
    }
    text = lower(text)
    for char, rep in replacements.items():
        text = text.replace(char, rep)
    # Remove all non-word characters and replace spaces with hyphens
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s-]+', '-', text).strip('-')
    return text

def amount_to_words(amount: int) -> str:
    """Converts numerical amounts to written Azerbaijani words."""
    if amount == 0:
        return "sıfır"
        
    ones = ["", "bir", "iki", "üç", "dörd", "beş", "altı", "yeddi", "səkkiz", "doqquz"]
    tens = ["", "on", "iyirmi", "otuz", "qırx", "əlli", "altmış", "yetmiş", "səksən", "doxsan"]
    
    def convert_less_than_1000(n):
        words = []
        h = n // 100
        if h > 0:
            if h > 1:
                words.append(ones[h])
            words.append("yüz")
        t = (n % 100) // 10
        o = n % 10
        if t > 0:
            words.append(tens[t])
        if o > 0:
            words.append(ones[o])
        return " ".join(words)

    result = []
    
    millions = amount // 1000000
    if millions > 0:
        result.append(convert_less_than_1000(millions))
        result.append("milyon")
    
    thousands = (amount % 1000000) // 1000
    if thousands > 0:
        if thousands > 1:
            result.append(convert_less_than_1000(thousands))
        result.append("min")
        
    remainder = amount % 1000
    if remainder > 0:
        result.append(convert_less_than_1000(remainder))
        
    return " ".join(result).strip()
