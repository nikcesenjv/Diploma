# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_object.py

from .find_by_main_folder import find_by_main_folder
from .find_by_inner_folder import find_by_inner_folder
from .find_by_file import find_by_file

from src.logging import log

FIND_START = "find_objects.start"

def find_object(data, type_of_object, params):
    log("INFO", FIND_START)

    match type_of_object:
        case "main":
            return find_by_main_folder(data[0], params)
        case "inner":
            return find_by_inner_folder(data[1], params)
        case "file":
            return find_by_file(data[2], params)
