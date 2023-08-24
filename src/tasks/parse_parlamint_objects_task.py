# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parse_parlamint_objects_task.py

from src.logging import log

from src.management.parlamint_objects_management import create_parlamint_document

from src.objects.general_objects import Document
from src.objects.parlamint_objects import ParlamintDocument, ParlamintAttendee

def parse_parlamint_objects_task(files: list[Document], attendees: list[ParlamintAttendee]) -> ParlamintDocument:
    log("INFO", "")
    return execute_task(files, attendees)

def execute_task(files: list[Document], all_attendees: list[ParlamintAttendee]) -> ParlamintDocument:
    # docx_documents = [create_parlamint_document(create_docx_object(file), attendees) for file in files]
    """parlamint_documents_list = []
    for file in files:
        parlamint_document, all_attendees = create_parlamint_document(file, all_attendees)
        parlamint_documents_list.append(parlamint_document)"""

    return create_parlamint_document(files[0], all_attendees)

    # parlamint_documents = [create_parlamint_object(create_docx_object(file), attendees) for file in files]
    # shelve_objects(parlamint_documents, "parlamint")

    # return parlamint_documents[0]
