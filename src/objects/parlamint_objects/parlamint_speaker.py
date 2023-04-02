# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_speaker.py

import xml.etree.ElementTree as ET

from .parlamint_note import ParlamintNote
from .parlamint_utterance import ParlamintUtterance

class ParlamintSpeaker:
    def __init__(self, note: ParlamintNote, utterance: ParlamintUtterance):
        self._note: ParlamintNote = note
        self._utterance: ParlamintUtterance = utterance

    @property
    def note(self) -> ParlamintNote:
        return self._note

    @note.setter
    def note(self, new_note: ParlamintNote) -> None:
        self._note = new_note

    @property
    def utterance(self) -> ParlamintUtterance:
        return self._utterance

    @utterance.setter
    def utterance(self, new_utterance: ParlamintUtterance) -> None:
        self._utterance = new_utterance

    def to_element(self, parent_element: ET):
        self.note.to_element(parent_element)
        self.utterance.to_element(parent_element)
