# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka directory_task.py

from src.retrieve_resources import retrieve_directory

def retrieve_directory_task(*directory_titles):
    return "/".join([retrieve_directory(directory_title) for directory_title in directory_titles])

def replace_directory_part_task(directory, old_title, new_title):
    return directory.replace(retrieve_directory(old_title), retrieve_directory(new_title))