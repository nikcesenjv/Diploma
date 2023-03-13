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
FIND_ERROR = "find_objects.parameter.error"

def find_objects_task(data, params):
    object_type, parsed_params = parse_params(params)
    candidates = find_object(data, object_type, parsed_params)

    if candidates:
        log("INFO", FIND_SUCCESS, len(candidates))
    else:
        log("WARNING", FIND_NONE)

    return candidates

def parse_params(params):
    return params[0], {params[i]: params[i + 1] for i in range(1, len(params), 2)}
