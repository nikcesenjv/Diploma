# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka file_parsing_task.py

import json

from src.parsing import *

class FileParsingTask:

    def __init__(self, path):
        self.path = path

        self.num_main_folders, self.num_inner_folders, self.num_files = 0, 0, 0

        self.directory, self.files = self.parse_json()

    def __str__(self):
        return f"Število glavnih map:   {self.num_main_folders}\n" \
               f"Število notranjih map: {self.num_inner_folders}\n" \
               f"Število datotek:       {self.num_files}"

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path

    def get_directory(self):
        return self.directory

    def set_directory(self, directory):
        self.directory = directory

    def get_files(self):
        return self.files

    def add_file(self, f):
        self.files.append(f)

    def add_files(self, files):
        self.files += files

    def get_num_main_folders(self):
        return self.num_main_folders

    def set_num_main_folders(self, num):
        self.num_main_folders = num

    def get_num_inner_folders(self):
        return self.num_inner_folders

    def set_num_inner_folders(self, num):
        self.num_inner_folders = num

    def get_num_files(self):
        return self.num_files

    def set_num_files(self, num):
        self.num_files = num

    def parse_json(self):
        try:
            directory, files_only = [], []
            num_main, num_inner, num_files = 0, 0, 0

            data = json.load(open(self.path))
            directory_path = self.get_path().replace("lib/datoteke.json", "documents/")

            for obj in data["documents"]:
                m_folder = MainFolder(obj["folder name"])
                m_folder.set_path(directory_path)

                for folder in obj["folders"]:
                    for inner, files in folder.items():
                        i_folder = InnerFolder(inner)
                        i_folder.set_path(m_folder.get_path())

                        for f in files:
                            pdf = File(f)
                            pdf.set_path(i_folder.get_path())
                            pdf.add_pdf()

                            pdf.set_outter_folder(i_folder)
                            i_folder.add_file(pdf)

                            files_only.append(pdf)

                        i_folder.set_outter_folder(m_folder)
                        m_folder.add_folder(i_folder)
                        num_inner += 1

                directory.append(m_folder)
                num_main += 1

            self.set_num_main_folders(num_main)
            self.set_num_inner_folders(num_inner)
            self.set_num_files(len(files_only))

            return directory, files_only

        except IsADirectoryError:
            print("Podana je bila napačna pot direktorija.")
        except json.decoder.JSONDecodeError:
            print("Podana je bila napačna vrsta datoteke.")
        except KeyError:
            print("Podana je bila napačna .json datoteka.")
