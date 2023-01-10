# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_message.py

import json

PROGRAM_MESSAGES = "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/src/resources/program_messages_sl.json"

def retrieve_message(level, name, args):
    for message_name, message_content in parse_json()[level].items():
        if message_name == name:
            return format_message(message_content, args)

def parse_json():
    return json.load(open(PROGRAM_MESSAGES))

def format_message(message, args):
    return message % args if len(args) > 0 else message

def change_language(lang):
    if lang == "en":
        PROGRAM_MESSAGES.replace("_sl.json", "_en.json")
