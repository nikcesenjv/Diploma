# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2021/2022
# Datoteka structure.py

class Structure:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def get_name(self):
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
        return self.path + ".txt"
