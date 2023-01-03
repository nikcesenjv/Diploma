# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_byfile.py

import logging

from src.retrieve_messages import retrieve_message

LOGGING_PATH = "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/updates.log"

logging.basicConfig(filename=LOGGING_PATH, level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s", datefmt="%d.%m.%Y %H:%M:%S")

class LoggingTask:
    def __init__(self, level, message_name, lang="sl"):
        self.level = level
        self.message_name = message_name
        self.lang = lang

        self.message_content = self.retrieve_message_content()

        self.generate_log()

    def retrieve_message_content(self):
        return retrieve_message(self.level, self.message_name)
        
    def generate_log(self):
        match self.level:
            case "INFO":
                logging.info(self.message_content)
            case "ERROR":
                logging.error(self.message_content)
            case "WARNING":
                logging.warning(self.message_content)
