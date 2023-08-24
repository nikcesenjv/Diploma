# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_parlamint_document.py

from .find_by_structure import *

from src.logging import log

from src.management.parlamint_objects_management.parlamint_attendee_management import is_attendee

from src.objects.general_objects import Document
from src.objects.parlamint_objects import ParlamintDocument

def find_by_parlamint_document(parlamint_document_list: list[ParlamintDocument], params: dict) \
        -> list[ParlamintDocument]:

    for attribute, value in params.items():
        try:
            func = globals()[METHOD_BASE + attribute]
            parlamint_document_list = func(parlamint_document_list, value)
        except KeyError:
            log("WARNING", "find_objects.key.error", attribute)

    log("INFO", "Najdenih '%s' Parlamint dokumentov.", len(parlamint_document_list))
    return parlamint_document_list

def find_by_file(parlamint_document_list: list[ParlamintDocument], file: Document):
    return [parlamint_document for parlamint_document in parlamint_document_list if parlamint_document.document == file]

def find_by_file_name(parlamint_document_list: list[ParlamintDocument], file_name: str) -> list[ParlamintDocument]:
    return [parlamint_document for parlamint_document in parlamint_document_list
            if parlamint_document.document.name == file_name]

def find_by_attendee(parlamint_document_list: list[ParlamintDocument], attendee_name: str) -> list[ParlamintDocument]:
    return [parlamint_document for parlamint_document in parlamint_document_list
            if is_attendee(attendee_name, parlamint_document.attendees)]

def find_by_utterance_num(parlamint_document_list: list[ParlamintDocument], utterance_num: str) \
        -> list[ParlamintDocument]:

    return [parlamint_document for parlamint_document in parlamint_document_list
            if parlamint_document.utterance_num == int(utterance_num)]

def find_by_segment_num(parlamint_document_list: list[ParlamintDocument], segment_num: str) -> list[ParlamintDocument]:
    return [parlamint_document for parlamint_document in parlamint_document_list
            if parlamint_document.segment_num == int(segment_num)]
