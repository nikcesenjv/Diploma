# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_row.py

import xml.etree.ElementTree as ET

from .namespace import Namespace

class DocxRow(Namespace):
    def __init__(self, row: ET):
        self._row: ET = row

        self._style: str = self.parse_style()
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
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text

    def is_bold(self) -> bool:
        # bold = self.row.find(".//w:b", self.NAMESPACE)
        return True if self.row.find(".//w:b", self.NAMESPACE) is not None else False

    # PARSING METHODS
    def parse_style(self) -> str:
        style_value = self.row.find(".//w:rStyle", self.NAMESPACE)
        """if style_value is not None:
            return list(style_value.attrib.values())[0]
        return None"""
        return list(style_value.attrib.values())[0] if style_value is not None else None

    def parse_text(self) -> str:
        text = self.row.findall(".//w:t", self.NAMESPACE)
        return "".join([t.text for t in text]).replace("-", "")


# self._text = self.parse_text()
# self._is_bold = self.check_if_bold()

"""def parse_text(self):
all_text_elements = self.row.findall(".//w:t", self.NAMESPACE)
return "".join([text_element.text for text_element in all_text_elements]).replace("-", "")

def check_if_bold(self):
return len(self.row.findall(".//w:b", self.NAMESPACE)) == 0"""

"""@property
    def text(self):
        return self._text

    @property
    def bold(self):
        return self._is_bold
"""