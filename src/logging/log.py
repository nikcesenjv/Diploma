# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka log.py

import logging

from .retrieve_message import retrieve_message

LOGGING_PATH = "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/updates.log"

logging.basicConfig(filename=LOGGING_PATH,
                    level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s",
                    datefmt="%d.%m.%Y %H:%M:%S",
                    filemode="w")

def log(level, message_title, *params):
    match level:
        case "INFO":
            logging.info(retrieve_message(level, message_title, params))
        case "ERROR":
            logging.error(retrieve_message(level, message_title, params))
        case "WARNING":
            logging.warning(retrieve_message(level, message_title, params))