# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parse_xml_objects_task.py

from src.logging import log

from src.management.path_management import *
from src.management.xml_management import create_parlamint_xml_document

from src.objects.parlamint_objects import ParlamintDocument

def parse_xml_objects_task(parlamint_documents: list[ParlamintDocument]) -> None:
    log("INFO", "")
    execute_task(parlamint_documents)

def execute_task(parlamint_documents: list[ParlamintDocument]) -> None:
    for parlamint_document in parlamint_documents:
        split_path = parlamint_document.docx_document.file.path.split("/")

        base_path = parse_path("full_path.documents", "xml")

        main_folder_path = parse_path(base_path, split_path[0])
        create_new_folder(main_folder_path)

        inner_folder_path = parse_path(main_folder_path, split_path[1])
        create_new_folder(inner_folder_path)

        create_parlamint_xml_document(parlamint_document, "x")

    """for main_folder in main_folders:
        main_folder_path = parse_path(base_path, main_folder.path)
        if not folder_exists(main_folder_path):
            create_new_folder(main_folder_path)

        for inner_folder in main_folder.folders:
            inner_folder_path = parse_path(base_path, inner_folder.path)
            if not os.path.isdir(inner_folder_path):
                create_new_folder(inner_folder_path)

            for file in inner_folder.files:
                # docx_document = DocxDocument(parse_path("full_path.documents", file.word_path))
                # docx_document = create_docx_object(file)
                # parlamint_document = create_parlamint_object(docx_document)
                # parlamint_document = ParlamintDocument(docx_document)
                # parlamint_documents.append(parlamint_document)
                # parlamint_documents.append(create_parlamint_object(create_docx_object(file)))
                parlamint_document = create_parlamint_object(create_docx_object(file))
                # parlamint_objects, utterances, segments = pa"""
