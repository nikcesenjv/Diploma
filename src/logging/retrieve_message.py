# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_message.py

from src.parsing import parse_json, parse_directory

PROJECT = "full_path.project"
MESSAGES_SL = "path.program_messages_sl"
BASIC_INFO = "path.basic_info.json"

def retrieve_message(level, name, args):
    messages_path = check_language()
    for message_name, message_content in parse_json(messages_path)[level].items():
        if message_name == name:
            return format_message(message_content, args)

def check_language():
    messages_path = parse_directory(PROJECT, MESSAGES_SL)
    if parse_json(parse_directory(PROJECT, BASIC_INFO))["basic info"]["language"] == "sl":
        return messages_path
    else:
        return messages_path.replace("_sl.json", "_en.json")

def format_message(message, args):
    return message % args if len(args) > 0 else message
