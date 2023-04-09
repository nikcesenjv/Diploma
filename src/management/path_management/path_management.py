# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka path_management.py

import os

from .retrieve_path import retrieve_path

from src.logging import log

def parse_path(*path_params: tuple[str]) -> str:
    return "/".join([retrieve_path(path_param) for path_param in path_params])

def replace_path_part(path: str, old_param: str, new_param: str) -> str:
    return path.replace(retrieve_path(old_param), retrieve_path(new_param))

def folder_exists(path: str) -> bool:
    if os.path.isdir(path):
        return True
    return False

def create_new_folder(path: str) -> None:
    os.mkdir(parse_path(path))
