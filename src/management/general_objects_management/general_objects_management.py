# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka general_objects_management.py

from src.management.path_management import parse_path

from src.objects.general_objects import Document, Folder, Book

def create_book(name: str) -> Book:
    return Book(name, name)

def create_document(name: str, path: str) -> Document:
    document = Document(name, f"{path}/{name}")
    # document.pages = document.get_num_of_pages(parse_path("full_path.documents", f"{document.pdf_path}"))
    return document

def create_folder(name: str, path: str) -> Folder:
    return Folder(name, f"{path}/{name}")
