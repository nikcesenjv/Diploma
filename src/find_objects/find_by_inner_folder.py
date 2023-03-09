# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_inner_folder.py

from .find_by_structure import *

from src.logging import log

def find_by_inner_folder(inner_folders, params):
    for attribute, value in params.items():
        try:
            func = globals()[METHOD_BASE + attribute]
            inner_folders = func(inner_folders, value)
        except KeyError:
            log("WARNING", "find_objects.key.error", attribute)

    return inner_folders

def find_by_num(inner_folders, num):
    return [inner_folder for inner_folder in inner_folders if inner_folder.num == num]

def find_by_spec_num(inner_folders, num):
    return [inner_folder for inner_folder in inner_folders if num in inner_folder.num]

def find_by_meeting(inner_folders, meeting):
    return [inner_folder for inner_folder in inner_folders if inner_folder.meeting == meeting]
