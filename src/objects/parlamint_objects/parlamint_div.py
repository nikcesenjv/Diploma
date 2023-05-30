# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_div.py

import xml.etree.ElementTree as ET

from .parlamint_head import ParlamintHead
from .parlamint_note import ParlamintNote
from .parlamint_speaker import ParlamintSpeaker

class ParlamintDiv:
    def __init__(self, div_type: str):
        self._div_type: str = div_type

        self._elements: list[ParlamintDiv, ParlamintHead | ParlamintNote | ParlamintSpeaker] = []

    @property
    def div_type(self) -> str:
        return self._div_type

    @div_type.setter
    def div_type(self, new_div_type: str) -> None:
        self._div_type = new_div_type

    @property
    def elements(self) -> list[ParlamintHead | ParlamintNote | ParlamintSpeaker]:
        return self._elements

    @elements.setter
    def elements(self, new_elements: list[ParlamintHead | ParlamintNote | ParlamintSpeaker]) -> None:
        self._elements = new_elements

    def add_element(self, new_element: ParlamintHead | ParlamintNote | ParlamintSpeaker) -> None:
        self._elements.append(new_element)

    def add_elements(self, new_elements: list[ParlamintHead | ParlamintNote | ParlamintSpeaker]) -> None:
        self._elements.extend(new_elements)

    def to_element(self, parent_element: ET) -> ET:
        div = ET.SubElement(parent_element, "div")

        if self.div_type is not None:
            div.set("type", self.div_type)

        for element in self.elements:
            element.to_element(div)

        return div
