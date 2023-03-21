# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_file.py

from .find_by_structure import *

from src.logging import log

from src.management.numerals_management import convert_numerals
from src.objects.general_objects import File

def find_by_file(files: list[File], params: dict) -> list[File]:
    for attribute, value in params.items():
        try:
            func = globals()[METHOD_BASE + attribute]
            files = func(files, value)
        except KeyError:
            log("WARNING", "find_objects.key.error", attribute)

    return files

def find_by_index(files: list[File], index: str) -> list[File]:
    return [file for file in files if file.index == int(index)]

def find_by_num(files: list[File], num: str) -> list[File]:
    return [file for file in files if convert_numerals(file.num.split(".")[0]) == num]

def find_by_assembly(files: list[File], assembly: str) -> list[File]:
    return [file for file in files if file.assembly == assembly]

def find_by_meeting(files: list[File], meeting: str) -> list[File]:
    return [file for file in files if file.meeting == meeting]

def find_by_date(files: list[File], date: str) -> list[File]:
    return [file for file in files if file.date == date]

def find_by_year(files: list[File], year: str) -> list[File]:
    return [file for file in files if file.year == year]

def find_by_pages(files: list[File], pages: str) -> list[File]:
    return [file for file in files if file.pages == pages]
