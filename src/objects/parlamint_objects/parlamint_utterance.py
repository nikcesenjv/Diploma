# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_utterance.py

import xml.etree.ElementTree as ET

from nltk import tokenize

from .parlamint_attendee import ParlamintAttendee
from .parlamint_segment import ParlamintSegment

class ParlamintUtterance:
    def __init__(self, attendee: ParlamintAttendee, document_id: str,
                 utterance_num: int, text: str, segments: bool = True):
        self._attendee: ParlamintAttendee = attendee
        self._document_id: str = document_id
        self._utterance_num: int = utterance_num
        self._text: str = text
        self._segments: bool = segments

        self._segment_text: list[ParlamintSegment] = self.parse_segments()

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
    def segments(self) -> bool:
        return self._segments

    @segments.setter
    def segments(self, new_segments: bool) -> None:
        self._segments = new_segments

    def parse_segments(self) -> list[ParlamintSegment]:
        if self.segments:
            segment_list = []
            for i, text_segment in enumerate(tokenize.sent_tokenize(self.text)):
                print(i)
                # segment_num = i +
                # segment = ParlamintSegment(self.document_id, )
            # return [ParlamintSegment(self.document_id, text_segment) for text_segment in tokenize.sent_tokenize(self.text)]
        else:
            return None

    def utterance_id(self):
        return f"{self.document_id}.u{self.utterance_num}"

    def to_element(self, parent_element: ET) -> None:
        utterance = ET.SubElement(parent_element, "u", who=self.attendee.id)
        utterance.set("xml:id", self.utterance_id())
        utterance.set("ana", f"#{self.attendee.type}")

        # self.split(utterance) if self.is_split_segments else utterance.text = self.text

    """def split(self, parent_element: ET) -> None:
        parent_element.text = self.text"""
