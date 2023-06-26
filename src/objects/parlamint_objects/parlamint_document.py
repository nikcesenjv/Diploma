# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_document.py

import xml.etree.ElementTree as ET

from docx import Document

from .parlamint_attendee import ParlamintAttendee
from .parlamint_head import ParlamintHead
from .parlamint_note import ParlamintNote
from .parlamint_speaker_list import ParlamintSpeakerList

from src.management.path_management import parse_path

from src.objects.general_objects import File

class ParlamintDocument:
    def __init__(self, file: File):
        self._file: File = file

        self._docx_document: Document = Document(parse_path("path.documents", file.word_path))
        self._document_id = f"ParlaMint-SR_{self.file.document_id}"

        self._attendees: list[ParlamintAttendee] = []
        self._elements: list[ParlamintHead | ParlamintNote | ParlamintSpeakerList] = []

        self._utterance_num: int = 0
        self._segment_num: int = 0

        # self._attendees_by_name: list[str] = []

        # self._xml_element: ET = None

    # GETTERS & SETTERS
    @property
    def file(self) -> File:
        return self._file

    @file.setter
    def file(self, new_file: File) -> None:
        self._file = new_file

    @property
    def docx_document(self) -> Document:
        return self._docx_document

    @docx_document.setter
    def docx_document(self, new_docx_document: Document) -> None:
        self._docx_document = new_docx_document

    @property
    def document_id(self) -> str:
        return self._document_id

    @document_id.setter
    def document_id(self, new_document_id: str) -> None:
        self._document_id = new_document_id

    @property
    def attendees(self) -> list[ParlamintAttendee]:
        return self._attendees

    @attendees.setter
    def attendees(self, new_attendees_list: list[ParlamintAttendee]) -> None:
        self._attendees = new_attendees_list

    def add_attendee(self, new_attendee: ParlamintAttendee) -> None:
        self._attendees.append(new_attendee)

    def add_attendees(self, new_attendees_list: list[ParlamintAttendee]) -> None:
        self._attendees += new_attendees_list

    @property
    def elements(self) -> list[ParlamintHead | ParlamintNote | ParlamintSpeakerList]:
        return self._elements

    @elements.setter
    def elements(self, new_elements: list[ParlamintHead | ParlamintNote | ParlamintSpeakerList]) -> None:
        self._elements = new_elements

    def add_element(self, new_element: ParlamintHead | ParlamintNote | ParlamintSpeakerList) -> None:
        self._elements.append(new_element)

    def add_elements(self, new_elements: list[ParlamintHead | ParlamintNote | ParlamintSpeakerList]) -> None:
        self._elements.extend(new_elements)

    @property
    def utterance_num(self) -> int:
        return self._utterance_num

    @utterance_num.setter
    def utterance_num(self, new_utterance_num: int) -> None:
        self._utterance_num = new_utterance_num

    @property
    def segment_num(self) -> int:
        return self._segment_num

    @segment_num.setter
    def segment_num(self, new_segment_num: int) -> None:
        self._segment_num = new_segment_num

    """@property
    def attendees_by_name(self) -> list[str]:
        return self._attendees_by_name

    @attendees_by_name.setter
    def attendees_by_name(self, new_attendees_by_name: list[str]) -> None:
        self._attendees_by_name = new_attendees_by_name

    def add_attendee_by_name(self, new_attendee_by_name: str) -> None:
        self._attendees_by_name.append(new_attendee_by_name)

    def add_attendees_by_name(self, new_attendees_by_name: list[str]) -> None:
        self._attendees_by_name += new_attendees_by_name

    def parse_attendees_by_name(self) -> None:
        for attendee_by_name in self.attendees:
            self.add_attendee_by_name(attendee_by_name)

    def find_attendee(self, target_attendee: str) -> ParlamintAttendee:
        real_attendee = get_close_matches(target_attendee, self.attendees_by_name, n=1)[0]

        for attendee in self.attendees:
            if attendee.name == real_attendee:
                return attendee"""

    """def add_object(self, new_object: ParlamintHead | ParlamintNote | ParlamintSpeakerList) -> None:
        self._objects.append(new_object)

        if type(new_object) == ParlamintSpeakerList:
            self.add_utterance()

    def add_objects(self, new_objects: list[ParlamintHead | ParlamintNote | ParlamintSpeakerListList]) -> None:
        self._objects += new_objects

    @property
    def num_of_utterances(self) -> int:
        return self._num_of_utterances

    @num_of_utterances.setter
    def num_of_utterances(self, new_num_of_utterances: int) -> None:
        self._num_of_utterances = new_num_of_utterances

    def add_utterance(self) -> None:
        self._num_of_utterances += 1

    def add_utterances(self, num_of_utterances: int) -> None:
        self._num_of_utterances += num_of_utterances

    @property
    def num_of_segments(self) -> int:
        return self._num_of_segments

    @num_of_segments.setter
    def num_of_segments(self, new_num_of_segments: int) -> None:
        self._num_of_segments = new_num_of_segments

    def add_segment(self) -> None:
        self._num_of_segments += 1

    def add_segments(self, num_of_segments: int) -> None:
        self._num_of_segments += num_of_segments
            
    @property
    def xml_element(self) -> ET:
        return self._xml_element
    
    @xml_element.setter
    def xml_element(self, new_xml_element) -> None:
        self._xml_element = new_xml_element"""
