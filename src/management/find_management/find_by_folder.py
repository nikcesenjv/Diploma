# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_folder.py

from .find_by_structure import *

from src.logging import log

from src.objects.general_objects import Folder

def find_by_folder(folder_list: list[Folder], params: dict) -> list[Folder]:
    for attribute, value in params.items():
        try:
            func = globals()[METHOD_BASE + attribute]
            folder_list = func(folder_list, value)
        except KeyError:
            log("WARNING", "find_objects.key.error", attribute)

    return folder_list

def find_by_num(folder_list: list[Folder], num: str) -> list[Folder]:
    return [folder for folder in folder_list if folder.num == num]

def find_by_spec_num(folder_list: list[Folder], num: str) -> list[Folder]:
    return [folder for folder in folder_list if num in folder.num]

def find_by_meeting(folder_list: list[Folder], meeting: str) -> list[Folder]:
    return [folder for folder in folder_list if folder.meeting == meeting]
