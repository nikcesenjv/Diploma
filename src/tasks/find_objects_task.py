# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_objects_task.py

from src.logging import log

from src.management.find_management import find_by_document, find_by_folder, find_by_book, \
    find_by_parlamint_document, parse_find_params

from src.objects.general_objects import Document, Folder, Book
from src.objects.parlamint_objects import ParlamintDocument, ParlamintAttendee

def find_objects_task(object_list: list[Document | Folder | Book | ParlamintDocument | ParlamintAttendee],
                      params: list[str]) \
        -> list[Document | Folder | Book | ParlamintDocument | ParlamintAttendee]:

    object_type, parsed_params = parse_find_params(params)
    candidates = execute_task(object_list, object_type, parsed_params)

    if candidates:
        log("INFO", "find_objects.success", len(candidates))
    else:
        log("WARNING", "find_objects.none", None)

    return candidates

def execute_task(object_list: list[Document | Folder | Book | ParlamintDocument | ParlamintAttendee],
                 type_of_object: str, params: dict[str, str]) \
        -> list[Document | Folder | Book | ParlamintDocument | ParlamintAttendee]:

    log("INFO", "find_objects.start", None)

    match type_of_object:
        case "document":
            return find_by_document(object_list, params)
        case "folder":
            return find_by_folder(object_list, params)
        case "book":
            return find_by_book(object_list, params)
        case "parlamint":
            return find_by_parlamint_document(object_list, params)
        case "attendee":
            ...
