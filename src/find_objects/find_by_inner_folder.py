# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_inner_folder.py

from .find_by_structure import *

METHOD_BASE = "find_by_"

def find_by_inner_folder(inner_folders, params):
    candidates = inner_folders
    for k, v in params.items():
        func = globals()[METHOD_BASE + k]

        candidates = func(candidates, v)

    return candidates

def find_by_name(inner_folders, name):
    return [inner_folder for inner_folder in inner_folders if inner_folder.get_name() == name]

def find_by_path(inner_folders, path):
    return [inner_folder for inner_folder in inner_folders if inner_folder.get_path() == path]

def find_by_num(inner_folders, num):
    return [inner_folder for inner_folder in inner_folders if inner_folder.get_num() == num]

def find_by_meeting(inner_folders, meeting):
    return [inner_folder for inner_folder in inner_folders if inner_folder.get_meeting() == meeting]
