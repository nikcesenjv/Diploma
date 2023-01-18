# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_directory.py

from ..json_parsing import parse_json

DIRECTORIES = "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/src/resources/directories.json"

def retrieve_directory(directory_title):
    try:
        return parse_json(DIRECTORIES)[directory_title]
    except KeyError:
        return directory_title
