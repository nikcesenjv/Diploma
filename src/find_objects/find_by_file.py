# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_file.py

from .find_by_structure import *
from src.tasks import ConvertNumeralsTask

def find_by_file(files, params):
    candidates = files
    for k, v in params.items():
        func = globals()[METHOD_BASE + k]

        candidates = func(candidates, v)

    return candidates

def find_by_index(files, index):
    return [file for file in files if index == file.get_index()]

def find_by_num(files, num):
    return [file for file in files if num == ConvertNumeralsTask(file.get_num().split(".")[0]).rim_to_arab()]

def find_by_meeting(files, meeting):
    return [file for file in files if meeting == file.get_meeting()]

def find_by_date(files, date):
    return [file for file in files if date == file.get_date()]
