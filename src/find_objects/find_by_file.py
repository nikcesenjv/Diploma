# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_file.py

from .find_by_structure import *
from src.tasks import convert_numerals_task

def find_by_file(files, params):
    candidates = files
    for k, v in params.items():
        func = globals()[METHOD_BASE + k]

        candidates = func(candidates, v)

    return candidates

def find_by_index(files, index):
    return [file for file in files if index == file.get_index()]

def find_by_num(files, num):
    return [file for file in files if num == convert_numerals_task(file.get_num().split(".")[0])]


def find_by_assembly(files, assembly):
    return [file for file in files if assembly == file.get_assembly()]

def find_by_meeting(files, meeting):
    return [file for file in files if meeting == file.get_meeting()]

def find_by_date(files, date):
    return [file for file in files if date == file.get_date()]

def find_by_year(files, year):
    return [file for file in files if year in file.get_date()]
