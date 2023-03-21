# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_structure.py

METHOD_BASE = "find_by_"

def find_by_name(objects: list[object], name: str):
    return [_object for _object in objects if _object.name == name]

def find_by_path(objects: list[object], path: str):
    return [_object for _object in objects if _object.path == path]
