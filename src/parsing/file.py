# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka file.py

from PyPDF2 import PdfFileReader

from .structure import Structure

class File(Structure):

    def __init__(self, name, path):
        super().__init__(name, path)

        self.index, self.num, self.assembly, self.meeting, self.date = self.parse_name()

        self.pages = 0
        self.outter_folder = None

    def __str__(self):
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

    def parse_name(self):
        parsed = self.name.split("_")
        return parsed[0], parsed[1], parsed[2], parsed[3], parsed[4]

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index

    def get_num(self):
        return self.num

    def parse_num(self):
        parsed_num = self.num.split(".")

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

        return self.num

    def set_num(self, num):
        self.num = num

    def get_meeting(self):
        return self.meeting

    def set_meeting(self, meeting):
        self.meeting = meeting

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_pages(self):
        return self.pages

    def set_pages(self, pages):
        self.pages = pages

    @staticmethod
    def get_num_of_pages(path):
        return str(PdfFileReader(open(path, "rb")).numPages)

    def get_outter_folder(self):
        return self.outter_folder

    def set_outter_folder(self, outter_folder):
        self.outter_folder = outter_folder
