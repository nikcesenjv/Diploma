# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka text_management.py

from cyrtranslit import to_latin
from difflib import get_close_matches
from io import StringIO

def cyrillic_to_latin_text(text: str) -> str:
    return to_latin(text, "sr")

def close_match(similar_words: list[str], text: str,) -> bool:
    text_split = text.split(" ")
    for similar_word in similar_words:
        if len(get_close_matches(similar_word, text_split)) > 0:
            return True
    return False

def write_text(full_path: str, text: str) -> None:
    with open(full_path, "w") as f:
        f.write(text)

def get_text(path):
    with open(path, "r") as file:
        return to_latin(file.read(), "sr")

def text_with_bold(rows, previous_bold: bool = False) -> str:
    _string = StringIO()

    for row_element in rows:
        if row_element.is_bold:
            if not previous_bold:
                _string.write(f"[{row_element.text}")
            else:
                _string.write(row_element.text)
        else:
            if not previous_bold:
                _string.write(row_element.text)
            else:
                _string = _string[:-1]
                _string.write(f"] {row_element.text}")

    if "[" in _string and "]" not in _string:
        _string.write("]")

    return _string.getvalue()
