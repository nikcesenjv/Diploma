# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_main_folder.py

from .find_by_structure import *

from src.logging import log

FIND_KEY_ERROR = "find_objects.key.error"

def find_by_main_folder(main_folders, params):
    candidates = main_folders
    for attribute, value in params.items():
        try:
            func = globals()[METHOD_BASE + attribute]
            candidates = func(candidates, value)
        except KeyError:
            log("WARNING", FIND_KEY_ERROR, attribute)

    return candidates

def find_by_index(main_folders, index):
    return [main_folder for main_folder in main_folders if index == main_folder.get_index()]

def find_by_year(main_folders, year):
    return [main_folder for main_folder in main_folders if year in main_folder.get_year()]

def find_by_assembly(main_folders, assembly):
    return [main_folder for main_folder in main_folders if assembly == main_folder.get_assembly()]