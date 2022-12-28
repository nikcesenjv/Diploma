# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main_folder.py

from .structure import Structure


class MainFolder(Structure):
    def __init__(self, name, path=None):
        super().__init__(name, path)

        self.index, self.year, self.org = self.parse_name()

        self.folders = []

    def __str__(self):
        return f"Ime mape:     {self.name}\n" \
               f"Indeks:       {self.index}\n" \
               f"Leto:         {self.year}\n" \
               f"Organizacija: {self.org}\n"

    def parse_name(self):
        parsed = self.name.split("_")
        return parsed[0], parsed[1], parsed[2]

    def get_index(self):
        return self.index

    def set_index(self, index):
        self.index = index

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_org(self):
        return self.org

    def set_org(self, org):
        self.org = org

    def get_folders(self):
        return self.folders

    def add_folder(self, folder):
        self.folders.append(folder)
