# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_note.py

import xml.etree.ElementTree as ET

from src.objects.docx_objects import DocxParagraph

class ParlamintNote:
    def __init__(self, note_type: str):
        self._note_type: str = note_type

        self._paragraphs: list[DocxParagraph] = []

    @property
    def note_type(self) -> str:
        return self._note_type

    @note_type.setter
    def note_type(self, new_note_type) -> None:
        self._note_type = new_note_type

    @property
    def paragraphs(self) -> list[DocxParagraph]:
        return self._paragraphs

    @paragraphs.setter
    def paragraphs(self, new_paragraphs: list[DocxParagraph]) -> None:
        self._paragraphs = new_paragraphs

    def add_paragraph(self, new_paragraph: DocxParagraph) -> None:
        self._paragraphs.append(new_paragraph)

    def add_paragraphs(self, new_paragraphs: list[DocxParagraph]) -> None:
        self._paragraphs.extend(new_paragraphs)

    def to_string(self) -> str:
        return "".join(self.paragraphs)

    def to_element(self, parent_element: ET) -> None:
        note = ET.SubElement(parent_element, "note", type=self.note_type)
        note.text = self.to_string()
