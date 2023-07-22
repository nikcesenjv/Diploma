# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_objects_task.py

from src.logging import log
from src.management.find_management import find_by_file, find_by_inner_folder, find_by_main_folder, \
    find_by_parlamint_document, parse_find_params

def find_objects_task(data: list[object], params: list[str]) -> list[object]:
    object_type, parsed_params = parse_find_params(params)
    candidates = execute_task(data, object_type, parsed_params)

    if candidates:
        log("INFO", "find_objects.success", len(candidates))
    else:
        log("WARNING", "find_objects.none")

    return candidates

def execute_task(data: list[object], type_of_object: str, params: dict) -> list[object]:
    log("INFO", "find_objects.start")

    match type_of_object:
        case "file":
            return find_by_file(data, params)
        case "inner":
            return find_by_inner_folder(data, params)
        case "main":
            return find_by_main_folder(data, params)
        case "parlamint":
            return find_by_parlamint_document(data, params)
