# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_cer_task.py

from cyrtranslit import to_latin
from jiwer import cer

"""class RetrieveCERTask:
    def __init__(self, error_path, correct_path):
        self.error_path = error_path
        self.correct_path = correct_path

        self.cer = self.retrieve_cer()

    def get_error_path(self):
        return self.error_path

    def set_error_path(self, error_path):
        self.error_path = error_path

    def get_correct_path(self):
        return self.correct_path

    def set_correct_path(self, correct_path):
        self.correct_path = correct_path
        
    def get_cer(self):
        return self.cer

    def retrieve_cer(self):
        return cer(self.open_file(self.get_error_path()), self.open_file(self.get_correct_path()))

    @staticmethod
    def open_file(file):
        with open(file, "r") as f:
            return to_latin(f.read(), "sr")"""

def retrieve_cer_task(first_path, second_path):
    return cer(get_text(first_path), get_text(second_path))

def get_text(path):
    with open(path, "r") as file:
        return to_latin(file.read(), "sr")
