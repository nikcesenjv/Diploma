# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_row.py

import xml.etree.ElementTree as ET

from src.management.text_management import cyrillic_to_latin_text

from docx import Document

class DocxRow:
    def __init__(self, row: Document):
        self._row: Document = row

        self._bold: bool = None
        self._font: str = None
        self._size: int = None

        self.parse_row_properties()

        self._text: str = self.parse_text()

    @property
    def row(self) -> Document:
        return self._row

    @row.setter
    def row(self, new_row: Document) -> None:
        self._row = new_row
        self.parse_row_properties()
        self.parse_text()

    @property
    def bold(self) -> bool:
        return self._bold

    @bold.setter
    def bold(self, is_bold: bool) -> None:
        self._bold = is_bold

    @property
    def font(self) -> str:
        return self._font

    @font.setter
    def font(self, new_font: str) -> None:
        self._font = new_font

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    def size(self, new_size: int) -> None:
        self._size = new_size

    def parse_row_properties(self) -> None:
        self.bold, self.font, self.size = self.row.bold, self.row.font, self.row.font.size

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text

    def parse_text(self):
        return cyrillic_to_latin_text(self.row.text)

    """def __init__(self, row: ET):
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

        return text"""
