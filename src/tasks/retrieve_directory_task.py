# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_directory_task.py

from src.retrieve_resources import retrieve_directory

class RetrieveDirectoryTask:
    def __init__(self, *directory_titles):
        self.directory_titles = directory_titles

    def get_directory_titles(self):
        return self.directory_titles

    def set_directory_title(self, directory_titles):
        self.directory_titles = directory_titles

    def retrieve_directory_content(self):
        return "".join([retrieve_directory(directory_title) for directory_title in self.directory_titles])
