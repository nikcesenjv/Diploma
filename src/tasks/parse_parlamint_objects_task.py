# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parse_parlamint_objects_task.py

import os

from src.logging import log

from src.management.path_management import parse_path, folder_exists, create_new_folder
from src.management.shelve_management import shelve_objects

from src.objects.docx_objects import DocxDocument
from src.objects.general_objects import MainFolder
from src.objects.parlamint_objects import ParlamintDocument

def parse_parlamint_objects_task(files: list[MainFolder]) -> list[ParlamintDocument]:
    log("INFO", "")
    execute_task(files)

def execute_task(main_folders: list[MainFolder]) -> None:
    parlamint_documents = []

    base_path = parse_path("full_path.documents", "xml")

    for main_folder in main_folders:
        main_folder_path = parse_path(base_path, main_folder.path)
        if not folder_exists(main_folder_path):
            create_new_folder(main_folder_path)

        for inner_folder in main_folder.folders:
            inner_folder_path = parse_path(base_path, inner_folder.path)
            if not os.path.isdir(inner_folder_path):
                create_new_folder(inner_folder_path)

            for file in inner_folder.files:
                docx_document = DocxDocument(parse_path("full_path.documents", file.word_path))
                parlamint_document = ParlamintDocument(docx_document)
                parlamint_documents.append(parlamint_document)

    shelve_objects(parlamint_documents, "parlamint")
