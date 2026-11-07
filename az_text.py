import re

CYRILLIC_TO_LATIN = {
    'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'Q', 'Ғ': 'Ğ', 'Д': 'D', 'Е': 'E', 'Ә': 'Ə',
    'Ж': 'J', 'З': 'Z', 'И': 'İ', 'Й': 'Y', 'Ј': 'Y', 'К': 'K', 'Ҝ': 'G', 'Л': 'L',
    'М': 'M', 'Н': 'N', 'О': 'O', 'Ө': 'Ö', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T',
    'У': 'U', 'Ү': 'Ü', 'Ф': 'F', 'Х': 'X', 'Һ': 'H', 'Ц': 'Ts', 'Ч': 'Ç', 'Ҹ': 'C',
    'Ш': 'Ş', 'Щ': 'Şç', 'Ы': 'I', 'Э': 'E', 'Ю': 'Yu', 'Я': 'Ya',
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'q', 'ғ': 'ğ', 'д': 'd', 'е': 'e', 'ә': 'ə',
    'ж': 'j', 'з': 'z', 'и': 'i', 'й': 'y', 'ј': 'y', 'к': 'k', 'ҝ': 'g', 'л': 'l',
    'м': 'm', 'н': 'n', 'о': 'o', 'ө': 'ö', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ү': 'ü', 'ф': 'f', 'х': 'x', 'һ': 'h', 'ц': 'ts', 'ч': 'ç', 'ҹ': 'c',
    'ш': 'ş', 'щ': 'şç', 'ы': 'ı', 'э': 'e', 'ю': 'yu', 'я': 'ya'
}

LATIN_TO_CYRILLIC = {
    'A': 'А', 'B': 'Б', 'V': 'В', 'Q': 'Г', 'Ğ': 'Ғ', 'D': 'Д', 'E': 'Е', 'Ə': 'Ә',
    'J': 'Ж', 'Z': 'З', 'İ': 'И', 'Y': 'Ј', 'K': 'К', 'G': 'Ҝ', 'L': 'Л', 'M': 'М',
    'N': 'Н', 'O': 'О', 'Ö': 'Ө', 'P': 'П', 'R': 'Р', 'S': 'С', 'T': 'Т', 'U': 'У',
    'Ü': 'Ү', 'F': 'Ф', 'X': 'Х', 'H': 'Һ', 'Ç': 'Ч', 'C': 'Ҹ', 'Ş': 'Ш', 'I': 'Ы',
    'a': 'а', 'b': 'б', 'v': 'в', 'q': 'г', 'ğ': 'ғ', 'd': 'д', 'e': 'е', 'ə': 'ә',
    'j': 'ж', 'z': 'з', 'i': 'и', 'y': 'ј', 'k': 'к', 'g': 'ҝ', 'l': 'л', 'm': 'м',
    'n': 'н', 'o': 'о', 'ö': 'ө', 'p': 'п', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у',
    'ü': 'ү', 'f': 'ф', 'x': 'х', 'h': 'һ', 'ç': 'ч', 'c': 'ҹ', 'ş': 'ш', 'ı': 'ы'
}

def cyrillic_to_latin(text: str) -> str:
    """Transliterator for Azerbaijani Cyrillic to Latin."""
    return ''.join(CYRILLIC_TO_LATIN.get(char, char) for char in text)

def latin_to_cyrillic(text: str) -> str:
    """Transliterator for Azerbaijani Latin to Cyrillic."""
    return ''.join(LATIN_TO_CYRILLIC.get(char, char) for char in text)

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
    """Converts non-negative integer amounts to written Azerbaijani words."""
    if isinstance(amount, bool) or not isinstance(amount, int):
        raise TypeError("amount must be an integer")
    if amount < 0:
        raise ValueError("amount must be non-negative")
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

    if amount >= 10**15:
        raise ValueError("amount must be less than 10**15")

    result = []

    trillions = amount // 10**12
    if trillions > 0:
        result.append(convert_less_than_1000(trillions))
        result.append("trilyon")

    billions = (amount % 10**12) // 1000000000
    if billions > 0:
        result.append(convert_less_than_1000(billions))
        result.append("milyard")

    millions = (amount % 1000000000) // 1000000
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
