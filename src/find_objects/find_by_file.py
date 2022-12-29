# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_file.py

from .find_by_structure import *
from src.tasks import ConvertNumeralsTask

METHOD_BASE = "find_by_"

def find_by_file(files, params):
    candidates = files
    for k, v in params.items():
        func = globals()[METHOD_BASE + k]

        candidates = func(candidates, v)

    return candidates

def find_by_index(files, index):
    return [file for file in files if file.get_index() == index]

def find_by_num(files, num):
    return [file for file in files if ConvertNumeralsTask(file.get_num()).rim_to_arab() == num]

def find_by_meeting(files, meeting):
    return [file for file in files if file.get_meeting() == meeting]

def find_by_date(files, date):
    return [file for file in files if file.get_date() == date]
