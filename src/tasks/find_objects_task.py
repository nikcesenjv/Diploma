# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_objects_task.py

from src.find_objects import find

class FindObjectsTask:
    def __init__(self, data, params):
        self.data = data
        self.params = params

        self.type_of_object, self.parsed_params = self.parse_params()

    def parse_params(self):
        return self.params[0], {self.params[i]: self.params[i + 1] for i in range(1, len(self.params), 2)}

    def get_type_of_object(self):
        return self.type_of_object

    def set_type_of_object(self, type_of_object):
        self.type_of_object = type_of_object

    def get_parsed_params(self):
        return self.parsed_params

    def get_candidates(self):
        return find(self.data, self.type_of_object, self.parsed_params)
