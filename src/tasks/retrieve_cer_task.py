# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_cer_task.py

import os
from jiwer import cer

import cyrtranslit

import convert_text_task

class RetrieveCERTask:
    def __init__(self, error_file_directory, correct_file_directory):
        self.error_file_directory = error_file_directory
        self.correct_file_directory = correct_file_directory

        # self.cer = self.retrieve_cer()

    def get_error_file_directory(self):
        return self.error_file_directory

    def set_error_file_directory(self, error_file_directory):
        self.error_file_directory = error_file_directory

    def get_correct_file_directory(self):
        return self.correct_file_directory

    def set_correct_file_directory(self, correct_file_directory):
        self.correct_file_directory = correct_file_directory

    """def get_cer(self):
        return self.cer"""

    def retrieve_cer(self):
        pass

    @staticmethod
    def open_file(file):
        with open(file, "r") as f:
            return f.read()
