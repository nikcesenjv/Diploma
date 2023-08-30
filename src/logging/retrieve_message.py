# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_message.py

from src.management.json_management import parse_json

def retrieve_message(level: str, message_title: str, arg: str) -> str:
    message_properties = "lib/resources/json/program_messages_en.json"
    for message_name, message_content in parse_json(message_properties)[level].items():
        if message_name == message_title:
            return format_message(message_content, arg)

def format_message(message: str, arg: str) -> str:
    return message % arg if arg is not None else message
