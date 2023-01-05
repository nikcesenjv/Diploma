# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_directory_task.py

from src.retrieve_resources import retrieve_directory

class RetrieveDirectoryTask:
    def __init__(self, directory_title):
        self.directory_title = directory_title

        self.directory_content = self.retrieve_directory_content()

    def __add__(self, other):
        return self.directory_content + other.directory_content

    def __str__(self):
        return self.directory_content

    def get_directory_title(self):
        return self.directory_title

    def set_directory_title(self, directory_title):
        self.directory_title = directory_title

    def retrieve_directory_content(self):
        return retrieve_directory(self.directory_title)
