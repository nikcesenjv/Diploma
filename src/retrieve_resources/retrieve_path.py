# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_path.py

import json

DIRECTORIES = "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/src/resources/directories.json"

def retreive_path(path_title):
    for path_name, path in parse_json().items():
        if path_name == path_title:
            return path

def parse_json():
    return json.load(open(DIRECTORIES))
