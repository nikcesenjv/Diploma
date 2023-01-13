# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_objects_task.py

from src.find_objects import find_object
from src.logging import log

# LOGGING VARIABLES
FIND_START = "find_objects.start"
FIND_SUCCESS = "find_objects.success"
FIND_NONE = "find_objects.none"

def find_objects_task(data, params):
    object_type, parsed_params = parse_params(params)
    candidates = find_object(data, object_type, parsed_params)

    if len(candidates) == 0:
        log("WARNING", FIND_NONE)
    else:
        log("INFO", FIND_SUCCESS, len(candidates))

    return candidates

def parse_params(params):
    return params[0], {params[i]: params[i + 1] for i in range(1, len(params), 2)}


"""class FindObjectsTask:

    # LOGGING VARIABLES
    FIND_START = "find_objects.start"
    FIND_SUCCESS = "find_objects.success"
    FIND_NONE = "find_objects.none"

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
        Log("INFO", self.FIND_START)
        candidates = find_object(self.data, self.type_of_object, self.parsed_params)

        if len(candidates) == 0:
            Log("WARNING", self.FIND_NONE)
        else:
            Log("INFO", self.FIND_SUCCESS, len(candidates))

        return candidates"""
