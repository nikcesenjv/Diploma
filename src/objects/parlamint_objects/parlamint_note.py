# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_note.py

import xml.etree.ElementTree as ET

from src.management.text_management import cyrillic_to_latin_text

class ParlamintNote:
    def __init__(self, note_type: str):
        self._note_type: str = note_type

        self._paragraphs = []
        self._text: str = None

    @property
    def note_type(self) -> str:
        return self._note_type

    @note_type.setter
    def note_type(self, new_note_type) -> None:
        self._note_type = new_note_type

    @property
    def paragraphs(self) -> list[str]:
        return self._paragraphs

    @paragraphs.setter
    def paragraphs(self, new_paragraphs: list[str]) -> None:
        self._paragraphs = new_paragraphs

    def add_paragraph(self, new_paragraph: str) -> None:
        self._paragraphs.append(new_paragraph)

    def add_paragraphs(self, new_paragraphs: list[str]) -> None:
        self._paragraphs.extend(new_paragraphs)

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text

    def to_string(self) -> str:
        self.text = " ".join(cyrillic_to_latin_text(paragraph.replace("-\n", "").replace("\n", " ")) for paragraph in self.paragraphs)
        return self.text

    def to_element(self, parent_element: ET) -> None:
        note = ET.SubElement(parent_element, "note", type=self.note_type)
        note.text = self.to_string()
