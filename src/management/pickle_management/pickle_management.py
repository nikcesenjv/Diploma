# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka shelve_management.py

import pickle

from src.objects.general_objects import Document, Folder, Book
from src.objects.parlamint_objects import ParlamintAttendee, ParlamintDocument

def open_pickle(type_of_object: str) -> list[Document | Folder | Book | ParlamintAttendee | ParlamintDocument]:
    with open(f"lib/resources/pickle/pickle_{type_of_object}.pkl", "rb") as f:
        x = pickle.load(f)
        return x

def pickle_objects(type_of_object: str,
                   object_list: list[Document | Folder | Book | ParlamintAttendee | ParlamintDocument]) -> None:

    with open(f"lib/resources/pickle/pickle_{type_of_object}.pkl", "wb") as f:
        pickle.dump(object_list, f)
