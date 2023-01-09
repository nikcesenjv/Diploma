# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka file_parsing_task.py

import json

from src.parsing import *
from .logging_task import LoggingTask as Log
from .replace_directory_part_task import ReplaceDirectoryPartTask

class FileParsingTask:

    # LOGGING MESSAGES
    PARSING_START = "file_parsing.start"
    PARSING_SUCCESS = "file_parsing.success"

    DIRECTORY_ERROR = "file_parsing.directory_error"
    DECODER_ERROR = "file_parsing.file_type_error"
    NO_FILE_ERROR = "file_parsing.no_file_error"
    KEY_ERROR = "file_parsing.key_error"

    # RETRIEVING DIRECTORIES
    DOCUMENTS_JSON = "path.documents.json"
    DOCUMENTS_PDF = "path.documents.pdf"

    def __init__(self, path):
        self.path = path

        self.num_main_folders, self.num_inner_folders, self.num_files = 0, 0, 0

        self.path_pdf = self.replace_directory_part()
        self.mains, self.inners, self.meetings = self.parse_json()

    def __str__(self):
        return f"Število glavnih map:   {self.num_main_folders}\n" \
               f"Število notranjih map: {self.num_inner_folders}\n" \
               f"Število datotek:       {self.num_files}"

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path

    def get_mains(self):
        return self.mains

    def set_mains(self, mains):
        self.mains = mains

    def get_inners(self):
        return self.inners

    def set_inners(self, inners):
        self.inners = inners

    def get_files(self):
        return self.meetings

    def add_file(self, f):
        self.meetings.append(f)

    def add_files(self, files):
        self.meetings += files

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

    def replace_directory_part(self):
        return ReplaceDirectoryPartTask(self.path, self.DOCUMENTS_JSON, self.DOCUMENTS_PDF).replace_directory_part()

    def parse_json(self):
        Log("INFO", self.PARSING_START, self.path.split("/")[-1])

        try:
            mains, inners, meetings = [], [], []

            data = json.load(open(self.path))

            for obj in data["documents"]:
                m_folder = MainFolder(obj["folder name"], f"/{obj['folder name']}")

                for folder in obj["folders"]:
                    for inner, files in folder.items():
                        i_folder = InnerFolder(inner, f"{m_folder.get_path()}/{inner}")

                        for m in files:
                            meeting = File(m, f"{i_folder.get_path()}/{m}")
                            meeting.set_pages(meeting.get_num_of_pages(self.path_pdf + meeting.get_path() + ".pdf"))

                            meeting.set_outter_folder(i_folder)
                            print(f"Datoteka '{meeting.get_name()}' ustvarjena")
                            i_folder.add_file(meeting)

                            meetings.append(meeting)

                        i_folder.set_outter_folder(m_folder)
                        m_folder.add_folder(i_folder)

                        inners.append(i_folder)

                mains.append(m_folder)

            self.set_num_main_folders(len(mains))
            self.set_num_inner_folders(len(inners))
            self.set_num_files(len(meetings))

            Log("INFO", self.PARSING_SUCCESS, self.path.split("/")[-1])

            return mains, inners, meetings

        except IsADirectoryError:
            Log("ERROR", self.DIRECTORY_ERROR)
            print("Podana je bila napačna pot direktorija.")
        except json.decoder.JSONDecodeError:
            Log("ERROR", self.DECODER_ERROR)
            print("Podana je bila napačna vrsta datoteke.")
        except KeyError:
            Log("ERROR", self.KEY_ERROR)
            print("Podana je bila napačna .json datoteka.")
        """except FileNotFoundError:
                    Log("ERROR", self.NO_FILE_ERROR, )"""
