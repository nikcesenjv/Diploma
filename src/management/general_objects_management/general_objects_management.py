# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka general_objects_management.py

from src.management.path_management import parse_path

from src.objects.general_objects import File, InnerFolder, MainFolder

def create_file(name: str, outter_folder: InnerFolder, path: str) -> File:
    file = File(name, f"{outter_folder.path}/{name}")
    file.pages = file.get_num_of_pages(parse_path(path, f"{file.pdf_path}"))
    file.outter_folder = outter_folder
    return file

def create_inner_folder(name: str, outter_path: MainFolder) -> InnerFolder:
    return InnerFolder(name, f"{outter_path}/{name}")

def create_main_folder(name: str) -> MainFolder:
    return MainFolder(name, name)
