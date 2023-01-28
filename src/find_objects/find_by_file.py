# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_file.py

from .find_by_structure import *

from src.logging import log
from src.parsing import convert_numerals

FIND_KEY_ERROR = "find_objects.key.error"

def find_by_file(files, params):
    for attribute, value in params.items():
        try:
            func = globals()[METHOD_BASE + attribute]
            files = func(files, value)
        except KeyError:
            log("WARNING", FIND_KEY_ERROR, attribute)

    return files

def find_by_index(files, index):
    return [file for file in files if index == file.get_index()]

def find_by_num(files, num):
    return [file for file in files if num == convert_numerals(file.get_num().split(".")[0])]

def find_by_assembly(files, assembly):
    return [file for file in files if assembly == file.get_assembly()]

def find_by_meeting(files, meeting):
    return [file for file in files if meeting == file.get_meeting()]

def find_by_date(files, date):
    return [file for file in files if date == file.get_date()]

def find_by_year(files, year):
    return [file for file in files if year in file.get_date()]

def find_by_year2(files, year):
    # return year in file.get_date()
    return filter(lambda file: year in file.get_date(), files)
