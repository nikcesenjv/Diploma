# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka file_parsing_task.py

import json

from .directory_task import replace_directory_part_task

from src.logging import log
from src.parsing import *

# DIRECTORIES
DOCUMENTS_JSON = "path.documents.json"
DOCUMENTS_PDF = "path.documents.pdf"

# MESSAGES
PARSING_PROGRESS = "file_parsing.progress"
PARSING_START = "file_parsing.start"
PARSING_SUCCESS = "file_parsing.success"

DIRECTORY_ERROR = "file_parsing.directory_error"
DECODER_ERROR = "file_parsing.file_type_error"
KEY_ERROR = "file_parsing.key_error"

def file_parsing_task(path):
    log("INFO", PARSING_START, path.split("/")[-1])
    return execute_parsing(path, replace_path(path, DOCUMENTS_JSON, DOCUMENTS_PDF))

def execute_parsing(path_json, path_pdf):
    log("INFO", PARSING_PROGRESS)
    all_files, all_inner_folders, all_main_folders = [], [], []
    data = open_json(path_json)

    for element in data["documents"]:
        current_main_folder = create_main_folder(element["folder name"])

        for folder in element["folders"]:
            for inner, files in folder.items():
                current_inner_folder = create_inner_folder(inner, current_main_folder.get_path())

                for note in files:
                    current_file = create_file(note, current_inner_folder.get_path(), path_pdf, current_inner_folder)
                    print(f"Datoteka {current_file.get_name()} ustvarjena")

                    current_inner_folder.add_file(current_file)
                    all_files.append(current_file)

                current_inner_folder.set_outter_folder(current_main_folder)
                current_main_folder.add_folder(current_inner_folder)

                all_inner_folders.append(current_inner_folder)

        all_main_folders.append(current_main_folder)

    return all_files, all_inner_folders, all_main_folders

def open_json(path):
    return json.load(open(path))

def replace_path(directory, old_content, new_content):
    return replace_directory_part_task(directory, old_content, new_content)

def create_main_folder(name):
    return MainFolder(name, f"/{name}")

def create_inner_folder(name, outter_path):
    return InnerFolder(name, f"{outter_path}/{name}")

def create_file(name, outter_path, full_path, outter_folder):
    current_file = File(name, f"{outter_path}/{name}")
    current_file.set_pages(current_file.get_num_of_pages(full_path + current_file.get_path() + ".pdf"))
    current_file.set_outter_folder(outter_folder)
    return current_file

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