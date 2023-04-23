# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_segment.py

import xml.etree.ElementTree as ET

class ParlamintSegment:
    def __init__(self, document_id: str, segment_num: int, text: str):
        self._document_id: str = document_id
        self._segment_num: int = segment_num
        self._text: str = text

    @property
    def document_id(self) -> str:
        return self._document_id

    @document_id.setter
    def document_id(self, new_xml_id: str) -> None:
        self._document_id = new_xml_id

    @property
    def segment_num(self) -> int:
        return self._segment_num

    @segment_num.setter
    def segment_num(self, new_segment_num: int) -> None:
        self._segment_num = new_segment_num

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text

    def segment_id(self) -> str:
        return f"{self.document_id}.seg{self.segment_num}"

    def to_element(self, parent_element: ET) -> None:
        segment = ET.SubElement(parent_element, "seg")
        segment.set("xml:id", self.segment_id())
        segment.text = self.text
