# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka shelve_management.py

import shelve

from src.objects.general_objects import File, InnerFolder, MainFolder
from src.objects.parlamint_objects import ParlamintDocument

def open_shelve(type_of_object: str):
    with shelve.open("objectsDB") as db:
        return db[type_of_object]

def shelve_objects(object_list: list[File | InnerFolder | MainFolder | ParlamintDocument], type_of_object: str) -> None:
    with shelve.open("objectsDB") as db:
        db[type_of_object] = object_list
