# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_path.py

from src.management.json_management import parse_json

DIRECTORIES = "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/src/resources/paths.json"

def retrieve_path(path_param):
    try:
        return parse_json(DIRECTORIES)[path_param]
    except KeyError:
        return path_param
