# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka log.py

import logging

from .retrieve_message import retrieve_message

logging.basicConfig(filename="updates.log", level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s",
                    datefmt="%d.%m.%Y %H:%M:%S", filemode="w")

def log(level: str, message_title: str, arg) -> None:
    match level:
        case "INFO":
            logging.info(retrieve_message(level, message_title, arg))
        case "ERROR":
            logging.error(retrieve_message(level, message_title, arg))
        case "WARNING":
            logging.warning(retrieve_message(level, message_title, arg))
