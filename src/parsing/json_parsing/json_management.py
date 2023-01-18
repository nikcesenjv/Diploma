# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka json_management.py

import json

def parse_json(path):
    return json.load(open(path))

def write_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

def change_json_value(path, key, value):
    data = parse_json(path)
    data["basic info"][key] = value
    write_json(path, data)
