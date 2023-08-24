# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_cer_task.py
import os

from jiwer import cer

from src.logging import log

from src.management.math_management import average
from src.management.text_management import get_text
from src.management.path_management import parse_path

# TODO: IMPROVE CODE [LESS IN main.py]
def retrieve_cer_task(params: list[str]) -> float:
    log("INFO", "retrieve_cer.start")
    # cer_average = average(execute_task(params))
    # log("INFO", "retrieve_cer.average", cer_average)
    return execute_task(params)

def execute_task(params: str) -> list[float]:
    # first_path, second_path = parse_path(params[0], params[1]), parse_path(params[0], params[2])
    first_path, second_path = params[0], params[1]

    """cer_list = []
    for first_file, second_file in zip(sorted(os.listdir(first_path)), sorted(os.listdir(second_path))):
        first_text, second_text = get_text(parse_path(first_path, first_file)), \
                                  get_text(parse_path(second_path, second_file))

        cer_list.append(cer(first_text, second_text))"""

    # return cer_list

    cer_dict = {}
    for first_file, second_file in zip(sorted(os.listdir(first_path)), sorted(os.listdir(second_path))):
        first_text, second_text = get_text(parse_path(first_path, first_file)), \
            get_text(parse_path(second_path, second_file))

        cer_dict[first_file] = cer(first_text, second_text)

    return cer_dict

"""def execute_arg_cer(params):
    try:
        first_path, second_path = parse_directory(PROJECT, DIRECTORY_LIB, params[0]), \
                                  parse_directory(PROJECT, DIRECTORY_LIB, params[1])

        return [retrieve_cer_task(parse_directory(first_path, first_file),
                                  parse_directory(second_path, second_file))
                                  for first_file, second_file in
                                  zip(sorted(os.listdir(first_path)), sorted(os.listdir(second_path)))]
    except FileNotFoundError:
        log("ERROR", "find_objects.index.error")
        return []"""
