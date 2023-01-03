# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main_folder.py

from .structure import Structure

class MainFolder(Structure):
    
    def __init__(self, name, path=None):
        super().__init__(name, path)

        self.index, self.year, self.assembly = self.parse_name()

        self.folders = []

    def __str__(self):
        return f"Ime mape:     {self.name}\n" \
               f"Indeks:       {self.index}\n" \
               f"Leto:         {self.year}\n" \
               f"Organizacija: {self.assembly}\n"

    def parse_name(self):
        parsed = self.name.split("_")
        return parsed[0], parsed[1], parsed[2]

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

    def get_assembly(self):
        return self.assembly

    def set_assembly(self, assembly):
        self.assembly = assembly

    def get_folders(self):
        return self.folders

    def add_folder(self, folder):
        self.folders.append(folder)

    def add_folders(self, folders):
        self.folders += folders
