# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_cer_task.py

from cyrtranslit import to_latin
from jiwer import cer

def retrieve_cer_task(first_path, second_path):
    return cer(get_text(first_path), get_text(second_path))

def get_text(path):
    with open(path, "r") as file:
        return to_latin(file.read(), "sr")
