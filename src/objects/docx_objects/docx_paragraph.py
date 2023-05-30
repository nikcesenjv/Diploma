# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_paragraph.py

import xml.etree.ElementTree as ET

from .docx_row import DocxRow

from docx import Document

class DocxParagraph:
    def __init__(self, paragraph: Document):
        self._paragraph: Document = paragraph

        self._rows: list[DocxRow] = self.parse_rows()

    @property
    def paragraph(self) -> Document:
        return self._paragraph

    @paragraph.setter
    def paragraph(self, new_paragraph: Document) -> None:
        self._paragraph = new_paragraph

    @property
    def rows(self) -> list[DocxRow]:
        return self._rows

    @rows.setter
    def rows(self, new_rows: list[DocxRow]) -> None:
        self._rows = new_rows

    def add_row(self, new_row: DocxRow) -> None:
        self._rows.append(new_row)

    def add_rows(self, new_rows: list[DocxRow]) -> None:
        self._rows.extend(new_rows)

    def parse_rows(self):
        return [DocxRow(row) for row in self.paragraph.runs]

    def parse_properties(self):
        """pr = []
        for run in self.paragraph.runs:
            properties = {
                "text": run.text,
                "bold": run.bold,
                "italic": run.italic,
                "underline": run.underline,
                "font": run.font.name,
                "size": run.font.size,
            }"""

    """def __init__(self, paragraph: ET):
        self._paragraph: ET = paragraph

        self._rows: list[DocxRow] = []

        self._text: str = None

    # GETTERS & SETTERS
    @property
    def paragraph(self) -> ET:
        return self._paragraph

    @paragraph.setter
    def paragraph(self, new_paragraph: ET) -> None:
        self._paragraph = new_paragraph

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

    def to_string(self, start: int = 0) -> str:
        # return "".join([row.text for row in self.rows])
        res = ""
        current_font_size = None
        first_new_line = False

        for row in self.rows[start:]:
            font_size = row.font_size
            if font_size != current_font_size:
                if not first_new_line:
                    res += row.text
                    first_new_line = True
                else:
                    res += f"\n{row.text}"
            else:
                res += row.text
            current_font_size = font_size

        return res"""

    """def parse_text_bold(self, previous_bold: bool = False) -> str:
        res = ""

        for row_element in self._rows:
            if row_element.is_bold():
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

        return res"""
