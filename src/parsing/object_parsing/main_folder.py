# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main_folder.py

from .structure import Structure

class MainFolder(Structure):
    def __init__(self, name, path):
        super().__init__(name, path)

        self._index, self._year, self._assembly = self.parse_name()

        self._folders = []

    # PRINT OBJECT INFO
    def __str__(self):
        return f"Ime mape:     {self.name}\n" \
               f"Indeks:       {self.index}\n" \
               f"Leto:         {self.year}\n" \
               f"Organizacija: {self.assembly}\n"

    # PARSING METHOD
    def parse_name(self):
        parsed = self.name.split("_")
        return parsed[0], parsed[1], parsed[2]

    # GETTERS & SETTERS
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, new_index):
        self._index = new_index

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, new_year):
        self._year = new_year

    @property
    def assembly(self):
        return self._assembly

    @assembly.setter
    def assembly(self, new_assembly):
        self._assembly = new_assembly

    @property
    def folders(self):
        return self._folders

    @folders.setter
    def folders(self, new_list):
        self._folders = new_list

    def add_folder(self, new_folder):
        self._folders.append(new_folder)

    def add_folders(self, new_folders):
        self._folders += new_folders

"""def __init__(self, name, path):
    super().__init__(name, path)

    self.index, self.year, self.assembly = self.parse_name()

    self.folders = []

# PRINT OBJECT
def __str__(self):
    return f"Ime mape:     {self.name}\n" \
           f"Indeks:       {self.index}\n" \
           f"Leto:         {self.year}\n" \
           f"Organizacija: {self.assembly}\n"

# PARSING METHOD
def parse_name(self):
    parsed = self.name.split("_")
    return parsed[0], parsed[1], parsed[2]

# GETTERS & SETTERS
def get_index(self):
    return self.index

def set_indes(self, index):
    self.index = index

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
    self.folders += folders"""
