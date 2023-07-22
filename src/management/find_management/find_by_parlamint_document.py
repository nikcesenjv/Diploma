# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_parlamint_document.py

from .find_by_structure import *

from src.logging import log

from src.management.parlamint_objects_management.parlamint_attendee_management import is_attendee

from src.objects.general_objects import File
from src.objects.parlamint_objects import ParlamintDocument

def find_by_parlamint_document(parlamint_documents: list[ParlamintDocument], params: dict) -> list[ParlamintDocument]:
    for attribute, value in params.items():
        try:
            func = globals()[METHOD_BASE + attribute]
            parlamint_documents = func(parlamint_documents, value)
        except KeyError:
            log("WARNING", "find_objects.key.error", attribute)

    log("INFO", "Najdenih '%s' Parlamint dokumentov.", len(parlamint_documents))
    return parlamint_documents

def find_by_file(parlamint_documents: list[ParlamintDocument], file: File):
    return [parlamint_document for parlamint_document in parlamint_documents if parlamint_document.file == file]

def find_by_file_name(parlamint_documents: list[ParlamintDocument], file_name: str) -> list[ParlamintDocument]:
    return [parlamint_document for parlamint_document in parlamint_documents
            if parlamint_document.file.name == file_name]

def find_by_attendee(parlamint_documents: list[ParlamintDocument], attendee_name: str) -> list[ParlamintDocument]:
    return [parlamint_document for parlamint_document in parlamint_documents
            if is_attendee(attendee_name, parlamint_document.attendees)]

def find_by_utterance_num(parlamint_documents: list[ParlamintDocument], utterance_num: str) -> list[ParlamintDocument]:
    return [parlamint_document for parlamint_document in parlamint_documents
            if parlamint_document.utterance_num == int(utterance_num)]

def find_by_segment_num(parlamint_documents: list[ParlamintDocument], segment_num: str) -> list[ParlamintDocument]:
    return [parlamint_document for parlamint_document in parlamint_documents
            if parlamint_document.segment_num == int(segment_num)]
