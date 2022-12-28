# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_structure.py

def find_by_name(data, name):
    return [d for d in data if d.get_name() == name]

def find_by_path(data, path):
    return [d for d in data if d.get_path() == path]