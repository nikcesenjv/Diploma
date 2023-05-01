# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_head.py

import xml.etree.ElementTree as ET

from src.objects.docx_objects import DocxParagraph

class ParlamintHead:
    def __init__(self, head_type: str):
        self._head_type: str = head_type

        self._paragraphs: list[DocxParagraph] = []

    @property
    def head_type(self) -> str:
        return self._head_type

    @head_type.setter
    def head_type(self, new_head_type: str) -> None:
        self._head_type = new_head_type

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
        if len(self.paragraphs) > 0:
            res = ""
            for paragraph in self.paragraphs:
                res += paragraph.text
            return res
        return ""

    def to_element(self, parent_element: ET):
        head = ET.SubElement(parent_element, "head")

        if self.head_type is not None:
            head.set("type", self.head_type)

        head.text = self.to_string()
