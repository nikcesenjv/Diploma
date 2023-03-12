# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_paragraph.py

import xml.etree.ElementTree as ET

from docx_row import DocxRow
from namespace import Namespace

class DocxParagraph(Namespace):
    def __init__(self, paragraph: ET):
        self._paragraph: ET = paragraph

        self._style: str | None = self.parse_style()
        self._rows:  list[DocxRow] = self.parse_rows()

        self._text: str = self.parse_text()

    # GETTERS & SETTERS
    @property
    def paragraph(self) -> ET:
        return self._paragraph

    @paragraph.setter
    def paragraph(self, new_paragraph: ET) -> None:
        self._paragraph = new_paragraph

    @property
    def style(self) -> str:
        return self._style

    @style.setter
    def style(self, new_style: str) -> None:
        self._style = new_style

    @property
    def rows(self) -> list[DocxRow]:
        return self._rows

    @rows.setter
    def rows(self, new_rows: list[DocxRow]) -> None:
        self._rows = new_rows

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text

    @property
    def text_with_bold_property(self) -> str:
        res = ""
        previous_bold = False

        for row_element in self._rows:
            is_bold = row_element.is_bold()

            if is_bold:
                if not previous_bold:
                    res += f"[{row_element.text}"
                else:
                    res += row_element.text
                previous_bold = True
            else:
                if not previous_bold:
                    res += row_element.text
                else:
                    res = res[:-1]
                    res += f"] {row_element.text}"
                previous_bold = False

        if "[" in res and "]" not in res:
            res += "]"

        """for row_element in self._rows:
            if row_element.is_bold and not previous_bold:
                res += f"[{row_element.text}"
                previous_bold = True
            elif row_element.is_bold and previous_bold:
                res += row_element.text
            else:
                if not previous_bold:
                    res += f"] {row_element.text}"
                else:
                    res += row_element.text
                previous_bold = False
"""
        return res

    # PARSING METHODS
    """def parse_text(self) -> str:
        return "".join([str(row.text) for row in self._rows])"""
    def parse_text(self) -> str:
        seznam = []
        for row in self.rows:
            x = row.text
            seznam.append(x)
        return "".join(seznam)

    def parse_style(self) -> str | None:
        style_value = self.paragraph.find(".//w:pStyle", self.NAMESPACE)
        if style_value is not None:
            return list(style_value.attrib.values())[0]
        return None

    def parse_rows(self) -> list[DocxRow]:  # row_elements = self.paragraph.findall(".//w:r", self.NAMESPACE)
        return [DocxRow(row_element) for row_element in self.paragraph.findall(".//w:r", self.NAMESPACE)]
