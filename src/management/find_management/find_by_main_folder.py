# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_main_folder.py

from .find_by_structure import *

from src.logging import log

from src.objects.general_objects import MainFolder

def find_by_main_folder(main_folders: list[MainFolder], params: dict) -> list[MainFolder]:
    for attribute, value in params.items():
        try:
            func = globals()[METHOD_BASE + attribute]
            main_folders = func(main_folders, value)
        except KeyError:
            log("WARNING", "find_objects.key.error", attribute)

    log("INFO", "Najdenih '%s' map.", len(main_folders))
    return main_folders

def find_by_index(main_folders: list[MainFolder], index: str) -> list[MainFolder]:
    return [main_folder for main_folder in main_folders if main_folder.index == int(index)]

def find_by_year(main_folders: list[MainFolder], year: str) -> list[MainFolder]:
    return [main_folder for main_folder in main_folders if year in main_folder.year]

def find_by_assembly(main_folders: list[MainFolder], assembly: str) -> list[MainFolder]:
    return [main_folder for main_folder in main_folders if main_folder.assembly == assembly]
