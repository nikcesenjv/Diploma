# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_directory.py

from .parse_json import parse_json

DIRECTORIES = "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/src/resources/directories.json"

def retrieve_directory(directory_title):
    """for directory_name, directory in parse_json().items():
        if directory_name == directory_title:
            return directory
    return None"""
    # return parse_json()[directory_title]
    try:
        data = parse_json(DIRECTORIES)
        return data[directory_title]
    except KeyError:
        return directory_title
