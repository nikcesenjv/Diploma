# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_directory_task.py

from src.retrieve_resources import retrieve_directory

from .logging_task import LoggingTask as Log

class FindDirectoryTask:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_name(self, name):
        self.name = name