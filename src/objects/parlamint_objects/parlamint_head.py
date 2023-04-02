# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_head.py

import xml.etree.ElementTree as ET

class ParlamintHead:
    def __init__(self, head_type: str, text: str):
        self._head_type: str = head_type
        self._text: str = text

    @property
    def head_type(self) -> str:
        return self._head_type

    @head_type.setter
    def head_type(self, new_head_type: str) -> None:
        self._head_type = new_head_type

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text

    def to_element(self, parent_element: ET) -> None:
        head = ET.SubElement(parent_element, "head")

        if self.head_type is not None:
            head.set("type", self.head_type)

        head.text = self.text
