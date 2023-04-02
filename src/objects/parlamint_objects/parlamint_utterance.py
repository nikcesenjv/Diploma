# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_utterance.py

import xml.etree.ElementTree as ET

from .parlamint_attendee import ParlamintAttendee

class ParlamintUtterance:
    def __init__(self, attendee: ParlamintAttendee, document_id: str, utterance_num: int, text: str):
        self._attendee: ParlamintAttendee = attendee
        self._document_id: str = document_id
        self._utterance_num: int = utterance_num
        self._text: str = text

        self._split_by_segments: bool = False

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
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text

    @property
    def is_split_segments(self) -> bool:
        return self._split_by_segments

    @is_split_segments.setter
    def is_split_segments(self, new_rule: bool) -> None:
        self._split_by_segments = new_rule

    def to_element(self, parent_element: ET) -> None:
        utterance = ET.SubElement(parent_element, "u", who=self.attendee.id)
        utterance.set("xml:id", f"{self.document_id}.u{self.utterance_num}")
        utterance.set("ana", f"#{self.attendee.type}")

        self.split(utterance) if self.is_split_segments else utterance.text = self.text

    def split(self, parent_element: ET) -> None:
        parent_element.text = self.text
