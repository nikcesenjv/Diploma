# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_by_document.py

from .find_by_structure import *

from src.logging import log

from src.management.numerals_management import convert_numerals
from src.objects.general_objects import Document

def find_by_document(document_list: list[Document], params: dict[str, str]) -> list[Document]:
    for attribute, value in params.items():
        try:
            func = globals()[METHOD_BASE + attribute]
            document_list = func(document_list, value)
        except KeyError:
            log("WARNING", "find_objects.key.error", attribute)

    return document_list

def find_by_index(document_list: list[Document], index: str) -> list[Document]:
    return [document for document in document_list if document.index == int(index)]

def find_by_num(document_list: list[Document], num: str) -> list[Document]:
    return [document for document in document_list if convert_numerals(document.num.split(".")[0]) == num]

def find_by_assembly(document_list: list[Document], assembly: str) -> list[Document]:
    return [document for document in document_list if document.assembly == assembly]

def find_by_meeting(document_list: list[Document], meeting: str) -> list[Document]:
    return [document for document in document_list if document.meeting == meeting]

def find_by_date(document_list: list[Document], date: str) -> list[Document]:
    return [document for document in document_list if document.date == date]

def find_by_year(document_list: list[Document], year: str) -> list[Document]:
    return [document for document in document_list if document.year == year]

def find_by_pages(document_list: list[Document], pages: str) -> list[Document]:
    return [document for document in document_list if document.pages == int(pages)]
