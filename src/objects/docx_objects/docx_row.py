# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_row.py

import xml.etree.ElementTree as ET

from src.management.text_management import cyrillic_to_latin_text

class DocxRow:
    def __init__(self, row: ET):
        self._row: ET = row

        self._is_bold: bool = None
        self._style: str = None
        self._font_size: int = None

        self._text: str = None

    # GETTERS & SETTERS
    @property
    def row(self) -> ET:
        return self._row

    @row.setter
    def row(self, new_row: ET) -> None:
        self._row = new_row

    @property
    def bold(self) -> bool:
        return self._is_bold

    @bold.setter
    def bold(self, new_bold_value: bool) -> None:
        self._is_bold = new_bold_value

    @property
    def style(self) -> str:
        return self._style

    @style.setter
    def style(self, new_style) -> None:
        self._style = new_style

    @property
    def font_size(self) -> int:
        return self._font_size

    @font_size.setter
    def font_size(self, new_font_size: int) -> None:
        self._font_size = new_font_size

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text

    def to_string(self) -> str:
        text = ""

        for element in self.row.iter():
            if element.text is not None:
                text += cyrillic_to_latin_text(element.text)
            elif "br" in element.tag:
                if text != "" and text[-1] == "-":
                    text = text[:-1]
                else:
                    text += " "
            elif "tab" in element.tag:
                text += "    "

        return text
