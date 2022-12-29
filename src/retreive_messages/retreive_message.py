# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retreive_message.py

import json

PROGRAM_MESSAGES = "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/src/resources/program_messages_sl.json"

def retreive_message(level, name):
    for message_name, message_content in parse_json()[level].items():
        if message_name == name:
            return message_content


def parse_json():
    return json.load(open(PROGRAM_MESSAGES))
