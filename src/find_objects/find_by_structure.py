# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_structure.py

METHOD_BASE = "find_by_"

def find_by_name(objects, name):
    return [object_type for object_type in objects if object_type.get_name() == name]

def find_by_path(objects, path):
    return [object_type for object_type in objects if object_type.get_path() == path]