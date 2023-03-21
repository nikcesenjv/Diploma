# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka file.py

from PyPDF2 import PdfReader

from .structure import Structure
from ..general_objects import InnerFolder

class File(Structure):
    def __init__(self, name, path):
        super().__init__(name, path)

        self._index, self._num, self._assembly, self._meeting, self._date = self.parse_name()

        self._pages: int = 0
        self._outter_folder: InnerFolder = None

    # PRINT OBJECT
    def __str__(self) -> str:
        info = f"Ime datoteke:       {self.name}\n" \
               f"Indeks:             {self.index}\n" \
               f"Št sestanka [rim.]: {self.parse_num()}\n" \
               f"Organizacija:       {self.assembly}\n" \
               f"Vrsta sestanka:     {self.meeting}\n" \
               f"Datum:              {self.date}\n" \
               f"Direktorij:         {self.path}\n"

        if self.pages == 0:
            return info + "Št strani:          ni znano\n"

        return info + f"Št strani:          {self.pages}\n"

    # PARSE METHODS
    def parse_name(self) -> tuple[int, str, str, str, str]:
        parsed = self.name.split("_")
        return int(parsed[0]), parsed[1], parsed[2], parsed[3], parsed[4]

    def parse_num(self) -> str:
        parsed_num = self._num.split(".")

        if len(parsed_num) == 2:
            second_part = None

            match parsed_num[1]:
                case "I":
                    second_part = "prvi"
                case "II":
                    second_part = "drugi"
                case "III":
                    second_part = "tretji"

            return f"{parsed_num[0]}, {second_part} del"

        return self._num

    @staticmethod
    def get_num_of_pages(full_path) -> int:
        return len(PdfReader(open(full_path, "rb")).pages)

    # GETTERS & SETTERS
    @property
    def pdf_path(self) -> str:
        return f"pdf/{self.path}.pdf"

    @property
    def txt_path(self) -> str:
        return f"txt/{self.path}.txt"

    @property
    def word_path(self) -> str:
        return f"word/{self.path}.docx"

    @property
    def xml_path(self) -> str:
        return f"xml/{self.path}.xml"

    @property
    def index(self) -> str:
        return self._index

    @index.setter
    def index(self, new_index: int | str) -> None:
        self._index = str(new_index)

    # TODO: rim. --> arab.
    @property
    def num(self) -> str:
        return self._num

    @num.setter
    def num(self, new_num: str) -> None:
        self._num = new_num

    @property
    def assembly(self) -> str:
        return self._assembly

    @assembly.setter
    def assembly(self, new_assembly: str) -> None:
        self._assembly = new_assembly

    @property
    def meeting(self) -> str:
        return self._meeting

    @meeting.setter
    def meeting(self, new_meeting: str) -> None:
        self._meeting = new_meeting

    @property
    def date(self) -> str:
        return self._date

    @date.setter
    def date(self, new_date: str) -> None:
        self._date = new_date

    @property
    def year(self) -> str:
        return self._date.split(".")[-1]

    @property
    def pages(self) -> int:
        return self._pages

    @pages.setter
    def pages(self, new_num_of_pages: int) -> None:
        self._pages = new_num_of_pages

    @property
    def outter_folder(self) -> InnerFolder:
        return self._outter_folder

    @outter_folder.setter
    def outter_folder(self, new_outter_folder: InnerFolder) -> None:
        self._outter_folder = new_outter_folder
