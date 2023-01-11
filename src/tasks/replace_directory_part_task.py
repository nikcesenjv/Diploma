# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka replace_directory_part_task.py

from .retrieve_directory_task import RetrieveDirectoryTask

class ReplaceDirectoryPartTask:
    def __init__(self, directory, old_content, new_content):
        self.directory = directory
        self.old_content = old_content
        self.new_content = new_content

        self.replaced = self.replace_directory_part()

    def __str__(self):
        return self.replaced()

    def get_directory(self):
        return self.directory

    def set_directory(self, directory):
        self.directory = directory

    def get_old_content(self):
        return self.old_content

    def set_old_content(self, old_content):
        self.old_content = old_content

    def get_new_content(self):
        return self.new_content

    def set_new_content(self, new_content):
        self.new_content = new_content

    def get_replaced(self):
        return self.replaced

    def replace_directory_part(self):
        return self.directory.replace(RetrieveDirectoryTask(self.old_content).retrieve_directory_content(),
                                      RetrieveDirectoryTask(self.new_content).retrieve_directory_content())
