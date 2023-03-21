# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka path_management.py

from .retrieve_path import retrieve_path

def parse_path(*path_params: tuple[str]) -> str:
    return "/".join([retrieve_path(path_param) for path_param in path_params])

def replace_path_part(path: str, old_param: str, new_param: str):
    return path.replace(retrieve_path(old_param), retrieve_path(new_param))
