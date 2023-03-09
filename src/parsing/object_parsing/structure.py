# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka structure.py

class Structure:
    def __init__(self, name, path):
        self._name = name
        self._path = path

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, new_path):
        self._path = new_path

"""def get_name(self):
    return self.name

def set_name(self, name):
    self.name = name

def get_path(self):
    return self.path

def set_path(self, path):
    self.path = path + f"{self.name}/"

def add_pdf(self):
    return self.path + ".pdf"

def add_txt(self):
    return self.path + ".txt"""
