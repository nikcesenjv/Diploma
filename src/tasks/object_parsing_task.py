# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka object_parsing_task.py

from src.logging import log
from src.parsing import *

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

def object_parsing_task(path):
    log("INFO", PARSING_START, path.split("/")[-1])
    return execute_parsing(path, replace_directory_part(path, DOCUMENTS_JSON, DOCUMENTS_PDF))

def execute_parsing(path_json, path_pdf):
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

    return all_files, all_inner_folders, all_main_folders

def create_main_folder(name):
    return MainFolder(name, name)

def create_inner_folder(name, outter_path):
    return InnerFolder(name, f"{outter_path}/{name}")

def create_file(name, outter_folder, path_pdf):
    current_file = File(name, f"{outter_folder.path}/{name}")
    meeting_full_path = parse_directory(path_pdf, f"{current_file.path}.pdf")
    current_file.pages = current_file.get_num_of_pages(meeting_full_path)
    current_file.outter_folder = outter_folder
    return current_file

"""def create_file(name, outter_path, full_path, outter_folder):
    current_file = File(name, f"{outter_path}/{name}")
    meeting_full_path = parse_directory(full_path, f"{current_file.get_path()}.pdf")
    current_file.set_pages(current_file.get_num_of_pages(meeting_full_path))
    current_file.set_outter_folder(outter_folder)
    return current_file"""

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