from src.management.path_management import parse_path
from src.objects.general_objects import File, InnerFolder, MainFolder

def create_main_folder(name):
    return MainFolder(name, name)

def create_inner_folder(name, outter_path):
    return InnerFolder(name, f"{outter_path}/{name}")

def create_file(name, outter_folder, path_pdf):
    current_file = File(name, f"{outter_folder.path}/{name}")
    meeting_full_path = parse_path(path_pdf, f"{current_file.path}.pdf")
    current_file.pages = current_file.get_num_of_pages(meeting_full_path)
    current_file.outter_folder = outter_folder
    return current_file
