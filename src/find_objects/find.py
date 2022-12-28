# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find.py

from .find_by_main_folder import find_by_main_folder
from .find_by_inner_folder import find_by_inner_folder
from .find_by_file import find_by_file

def find(data, type_of_object, params):
    match type_of_object:
        case "main":
            return find_by_main_folder(data.get_mains(), params)
        case "inner":
            return find_by_inner_folder(data.get_inners(), params)
        case "file":
            return find_by_file(data.get_files(), params)
