# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka directory_management.py

from .retrieve_directory import retrieve_directory

def add_pdf_to_name(name):
    return f"{name}.pdf"

def add_txt_to_name(name):
    return f"{name}.txt"

def add_word_to_name(name):
    return f"{name}.docx"

def add_pdf_to_path(path):
    return f"pdf/{path}.pdf"

def add_txt_to_path(path):
    return f"txt/{path}.pdf"

def add_word_to_path(path):
    return f"word/{path}.docx"

def parse_directory(*directory_titles):
    return "/".join([retrieve_directory(directory_title) for directory_title in directory_titles])

def replace_directory_part(directory, old_title, new_title):
    return directory.replace(retrieve_directory(old_title), retrieve_directory(new_title))
