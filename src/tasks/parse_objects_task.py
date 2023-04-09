# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parse_objects_task.py

from src.logging import log

from src.management.path_management import replace_path_part
from src.management.general_objects_management import *
from src.management.json_management import parse_json
from src.management.shelve_management import shelve_objects

# DIRECTORIES
PROJECT = "full_path.project"
DOCUMENTS_JSON = "path.documents.json"
DOCUMENTS_PDF = "path.documents.pdf"

# MESSAGES
PARSING_PROGRESS = "file_parsing.progress"
PARSING_START = "file_parsing.start"
PARSING_SUCCESS = "file_parsing.success"
PARSING_MAIN = "file_parsing.main_folder.success"

DIRECTORY_ERROR = "file_parsing.directory_error"
DECODER_ERROR = "file_parsing.file_type_error"
KEY_ERROR = "file_parsing.key_error"

def parse_objects_task(path: str) -> None:
    log("INFO", PARSING_START, path.split("/")[-1])
    # execute_task(path, replace_path_part(path, DOCUMENTS_JSON, DOCUMENTS_PDF))
    execute_task(path, parse_path("full_path.documents"))

def execute_task(path_json: str, path_pdf: str) -> None:
    log("INFO", PARSING_PROGRESS)

    all_files, all_inner_folders, all_main_folders = [], [], []
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
    shelve_objects(all_main_folders, "main")

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