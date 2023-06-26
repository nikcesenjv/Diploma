# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_speaker_list.py

import xml.etree.ElementTree as ET

from .parlamint_speaker import ParlamintSpeaker

class ParlamintSpeakerList:
    def __init__(self):
        self._parlamint_speakers: list[ParlamintSpeaker] = []

    @property
    def parlamint_speakers(self) -> list[ParlamintSpeaker]:
        return self._parlamint_speakers

    @parlamint_speakers.setter
    def parlamint_speakers(self, new_parlamint_speakers: list[ParlamintSpeaker]) -> None:
        self._parlamint_speakers = new_parlamint_speakers

    def add_parlamint_speaker(self, new_parlamint_speaker: ParlamintSpeaker) -> None:
        self._parlamint_speakers.append(new_parlamint_speaker)

    def add_parlamint_speakers(self, new_parlamint_speakers: list[ParlamintSpeaker]) -> None:
        self._parlamint_speakers.extend(new_parlamint_speakers)

    def to_element(self, parent_element: ET):
        for parlamint_element in self.parlamint_speakers:
            parlamint_element.to_element(parent_element)
