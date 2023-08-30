# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka retrieve_message.py

from src.management.json_management import parse_json
from src.management.path_management import parse_path

def retrieve_message(level: str, name: str, args: tuple[str]):
    messages_path = check_language()
    for message_name, message_content in parse_json(messages_path)[level].items():
        if message_name == name:
            return format_message(message_content, args)

def check_language() -> str:
    # messages_path = parse_path("full_path.project", "path.program_messages_sl")
    messages_path = "lib/resources/json/program_messages_sl.json"

    # if parse_json(parse_path("full_path.project", "path.basic_info.json"))["basic info"]["language"] == "sl":

    if parse_json("lib/resources/json/basic_info.json")["basic info"]["language"] == "sl":
        return messages_path
    else:
        return messages_path.replace("_sl.json", "_en.json")

def format_message(message: str, args: tuple[str]) -> str:
    return message % args if len(args) > 0 else message
