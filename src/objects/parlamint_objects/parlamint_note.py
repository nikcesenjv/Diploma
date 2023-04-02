# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_note.py

import xml.etree.ElementTree as ET

class ParlamintNote:
    def __init__(self, note_type: str, text: str):
        self._note_type: str = note_type
        self._text: str = text

    @property
    def note_type(self) -> str:
        return self._note_type

    @note_type.setter
    def note_type(self, new_note_type) -> None:
        self._note_type = new_note_type

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text) -> None:
        self._text = new_text

    def to_element(self, parent_element: ET) -> None:
        note = ET.SubElement(parent_element, "note", type=self.note_type)
        note.text = self.text
