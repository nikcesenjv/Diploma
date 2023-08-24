# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_book.py

from .find_by_structure import *

from src.logging import log

from src.objects.general_objects import Book

def find_by_book(book_list: list[Book], params: dict) -> list[Book]:
    for attribute, value in params.items():
        try:
            func = globals()[METHOD_BASE + attribute]
            book_list = func(book_list, value)
        except KeyError:
            log("WARNING", "find_objects.key.error", attribute)

    log("INFO", "Najdenih '%s' knjig", len(book_list))
    return book_list

def find_by_index(book_list: list[Book], index: str) -> list[Book]:
    return [book for book in book_list if book.index == int(index)]

def find_by_year(book_list: list[Book], year: str) -> list[Book]:
    return [book for book in book_list if year in book.year]

def find_by_assembly(book_list: list[Book], assembly: str) -> list[Book]:
    return [book for book in book_list if book.assembly == assembly]
