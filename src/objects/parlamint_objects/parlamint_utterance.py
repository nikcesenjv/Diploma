# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_utterance.py

import xml.etree.ElementTree as ET

from .parlamint_attendee import ParlamintAttendee

from src.management.text_management import cyrillic_to_latin_text

class ParlamintUtterance:
    def __init__(self, attendee: ParlamintAttendee):
        self._attendee: ParlamintAttendee = attendee

        self._document_id: str = None
        self._utterance_num: int = None
        self._segment_start_num: int = 1

        self._paragraphs: list[str] = []
        self._text: str = None

    @property
    def attendee(self) -> ParlamintAttendee:
        return self._attendee

    @attendee.setter
    def attendee(self, new_attendee) -> None:
        self._attendee = new_attendee

    @property
    def document_id(self) -> str:
        return self._document_id

    @document_id.setter
    def document_id(self, new_document_id: str) -> None:
        self._document_id = new_document_id

    @property
    def utterance_num(self) -> int:
        return self._utterance_num

    @utterance_num.setter
    def utterance_num(self, new_utterance_num: int) -> None:
        self._utterance_num = new_utterance_num

    @property
    def segment_start_num(self) -> int:
        return self._segment_start_num

    @segment_start_num.setter
    def segment_start_num(self, new_segment_start_num: int) -> None:
        self._segment_start_num = new_segment_start_num

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

    def to_string(self):
        self.text = " ".join(cyrillic_to_latin_text(paragraph) for paragraph in self.paragraphs)
        return self.text

    def to_element(self, parent_element: ET) -> None | int:
        # print(self.attendee.id)
        utterance = ET.SubElement(parent_element, "u", who=self.attendee.id)
        utterance.set("xml:id", f"{self.document_id}.u{self.utterance_num}")
        utterance.set("ana", f"#{self.attendee.attendee_role}")

        segment_counter = self.segment_start_num
        for paragraph in self.paragraphs:
            segment = ET.SubElement(utterance, "seg")
            segment.set("xml:id", f"{self.document_id}.seg{segment_counter}")
            segment.text = paragraph.replace("-\n", "").replace("-", "")

            segment_counter += 1
