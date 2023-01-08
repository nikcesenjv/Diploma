# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_cer_task.py

from jiwer import cer

class RetrieveCERTask:
    def __init__(self, error_file_path, correct_file_path):
        self.error_file_path = error_file_path
        self.correct_file_path = correct_file_path

        self.cer = self.retrieve_cer()

    def get_error_file_path(self):
        return self.error_file_path

    def set_error_file_path(self, error_file_path):
        self.error_file_path = error_file_path

    def get_correct_file_path(self):
        return self.correct_file_path

    def set_correct_file_path(self, correct_file_path):
        self.correct_file_path = correct_file_path

    def get_cer(self):
        return self.cer

    def retrieve_cer(self):
        return cer(self.open_file(self.error_file_path), self.open_file(self.correct_file_path))

    @staticmethod
    def open_file(file):
        with open(file, "r") as f:
            return f.read()
