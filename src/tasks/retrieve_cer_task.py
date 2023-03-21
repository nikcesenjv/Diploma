# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_cer_task.py

from jiwer import cer

from src.management.text_management import get_text

# TODO: IMPROVE CODE [LESS IN main.py]
def retrieve_cer_task(first_path: str, second_path: str) -> float:
    return cer(get_text(first_path), get_text(second_path))
