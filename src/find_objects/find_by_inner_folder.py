# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_inner_folder.py

from .find_by_structure import *

from src.logging import log

FIND_KEY_ERROR = "find_objects.key.error"

def find_by_inner_folder(inner_folders, params):
    candidates = inner_folders
    for attribute, value in params.items():
        try:
            func = globals()[METHOD_BASE + attribute]
            candidates = func(candidates, value)
        except KeyError:
            log("WARNING", FIND_KEY_ERROR, attribute)

    return candidates

def find_by_num(inner_folders, num):
    return [inner_folder for inner_folder in inner_folders if num in inner_folder.get_num()]

def find_by_meeting(inner_folders, meeting):
    return [inner_folder for inner_folder in inner_folders if meeting == inner_folder.get_meeting()]
