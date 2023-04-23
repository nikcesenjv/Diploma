# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_row.py

import xml.etree.ElementTree as ET

from .element_parser import ElementParser

from src.management.text_management import cyrillic_to_latin_text

class DocxRow(ElementParser):
    def __init__(self, row: ET):
        self._row: ET = row

        self._style: str = self.parse_style()
        self._font_size: int = self.parse_font_size()
        self._is_bold: bool = self.is_bold()

        self._text: str = self.parse_text()

    # GETTERS & SETTERS
    @property
    def row(self) -> ET:
        return self._row

    @row.setter
    def row(self, new_row: ET) -> None:
        self._row = new_row

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

    def is_bold(self) -> bool:
        return True if self.row.find(".//w:b", self.NAMESPACE) is not None else False

    # PARSING METHODS
    def parse_style(self) -> str:
        style_value = self.row.find(".//w:rStyle", self.NAMESPACE)
        return list(style_value.attrib.values())[0] if style_value is not None else None

    def parse_font_size(self) -> int:
        font_size = self.row.find(".//w:sz", self.NAMESPACE)
        return int(list(font_size.attrib.values())[0]) / 2 if font_size is not None else None

    def parse_text(self) -> str:
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
