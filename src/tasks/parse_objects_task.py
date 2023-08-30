# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parse_objects_task.py

from src.logging import log

from src.management.path_management import replace_path_part
from src.management.general_objects_management import *
from src.management.json_management import parse_json
from src.management.shelve_management import shelve_objects
from src.management.pickle_management import pickle_objects

def parse_objects_task() -> None:
    # log("INFO", PARSING_START, path.split("/")[-1])
    # execute_task(path, replace_path_part(path, DOCUMENTS_JSON, DOCUMENTS_PDF))
    execute_task()

def execute_task() -> None:
    # log("INFO", PARSING_PROGRESS)

    all_documents_list, all_folders_list, all_books_list = [], [], []
    # data = parse_json(parse_path("full_path.project", "path.documents.json"))
    data = parse_json("lib/resources/json/documents_info.json")

    for book in data["documents"]:
        current_book = create_book(book["book name"])

        for folder_list in book["folders"]:
            for folder, document_list in folder_list.items():
                current_folder = create_folder(folder, current_book.path)

                for document in document_list:
                    current_document = create_document(document, current_folder.path)
                    print(f"Dokument {current_document.name} ustvarjen")

                    current_folder.add_document(current_document)
                    all_documents_list.append(current_document)

                current_book.add_folder(current_folder)

        all_books_list.append(current_book)

    # shelve_objects(all_documents_list, "document")
    # shelve_objects(all_folders_list, "folder")
    # shelve_objects(all_books_list, "book")

    pickle_objects("document", all_documents_list)
    pickle_objects("folder", all_folders_list)
    pickle_objects("book", all_books_list)

    """all_files, all_inner_folders, all_main_folders = [], [], []
    data = parse_json(path_json)

    for _main_folder in data["documents"]:
        current_main_folder = create_main_folder(_main_folder["folder name"])

        for folder in _main_folder["folders"]:
            for _inner_folder, files in folder.items():
                current_inner_folder = create_inner_folder(_inner_folder, current_main_folder.path)

                for _file in files:
                    current_file = create_file(_file, current_inner_folder, path_pdf)
                    print(f"Datoteka {current_file.name} ustvarjena")

                    current_inner_folder.add_file(current_file)
                    all_files.append(current_file)

                current_inner_folder.outter_folder = current_main_folder
                current_main_folder.add_folder(current_inner_folder)

                all_inner_folders.append(current_inner_folder)

        all_main_folders.append(current_main_folder)

    shelve_objects(all_files, "file")
    shelve_objects(all_inner_folders, "inner")
    shelve_objects(all_main_folders, "main")"""

"""
        except IsADirectoryError:
            Log("ERROR", self.DIRECTORY_ERROR)
            print("Podana je bila napačna pot direktorija.")
        except json.decoder.JSONDecodeError:
            Log("ERROR", self.DECODER_ERROR)
            print("Podana je bila napačna vrsta datoteke.")
        except KeyError:
            Log("ERROR", self.KEY_ERROR)
            print("Podana je bila napačna .json datoteka.")
"""