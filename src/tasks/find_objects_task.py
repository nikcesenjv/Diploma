# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_objects_task.py

from src.logging import log
from src.management.find_management import find_by_document, find_by_folder, find_by_book, \
    find_by_parlamint_document, parse_find_params

def find_objects_task(data: list[object], params: list[str]) -> list[object]:
    object_type, parsed_params = parse_find_params(params)
    candidates = execute_task(data, object_type, parsed_params)

    """if candidates:
        log("INFO", "find_objects.success", len(candidates))
    else:
        log("WARNING", "find_objects.none")"""

    return candidates

def execute_task(data: list[object], type_of_object: str, params: dict) -> list[object]:
    log("INFO", "find_objects.start")

    match type_of_object:
        case "document":
            return find_by_document(data, params)
        case "folder":
            return find_by_folder(data, params)
        case "book":
            return find_by_book(data, params)
        case "parlamint":
            return find_by_parlamint_document(data, params)
