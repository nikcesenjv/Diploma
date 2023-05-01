# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parse_parlamint_objects_task.py

from src.logging import log

from src.management.docx_objects_management import create_docx_object
from src.management.parlamint_objects_management import create_parlamint_object
from src.management.shelve_management import shelve_objects

from src.objects.general_objects import File
from src.objects.parlamint_objects import ParlamintDocument

def parse_parlamint_objects_task(files: list[File]) -> ParlamintDocument:
    log("INFO", "")
    return execute_task(files)

def execute_task(files: list[File]) -> ParlamintDocument:
    parlamint_documents = [create_parlamint_object(create_docx_object(file)) for file in files]
    # shelve_objects(parlamint_documents, "parlamint")

    return parlamint_documents[0]
