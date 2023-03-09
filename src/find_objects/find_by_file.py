# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_file.py

from .find_by_structure import *

from src.logging import log
from src.parsing import convert_numerals

def find_by_file(files, params):
    for attribute, value in params.items():
        try:
            func = globals()[METHOD_BASE + attribute]
            files = func(files, value)
        except KeyError:
            log("WARNING", "find_objects.key.error", attribute)

    return files

def find_by_index(files, index):
    return [file for file in files if file.index == index]

def find_by_num(files, num):
    return [file for file in files if convert_numerals(file.num.split(".")[0]) == num]

def find_by_assembly(files, assembly):
    return [file for file in files if file.assembly == assembly]

def find_by_meeting(files, meeting):
    return [file for file in files if file.meeting == meeting]

def find_by_date(files, date):
    return [file for file in files if file.date == date]

def find_by_year(files, year):
    return [file for file in files if file.year == year]
