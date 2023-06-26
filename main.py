# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main.py

import argparse

from src.logging import log

from src.tasks import *

from src.management.json_management import change_json_value
from src.management.shelve_management import *
from src.management.path_management import parse_path
from src.management.xml_management import create_parlamint_xml_document

from src.objects.docx_objects import DocxDocument

# EXECUTE METHODS
def execute_arg_cer(params: list[str]) -> float:
    try:
        return retrieve_cer_task(params)
    except FileNotFoundError:
        log("ERROR", "file_parsing.directory.error")

def execute_arg_find(params: list[str]) -> list[object]:
    try:
        return find_objects_task(open_shelve(params[0]), params)
    except IndexError:
        log("ERROR", "find_objects.index.error")
        return []

def execute_arg_language(lang: str) -> None:
    supported_languages = ["sl", "en"]
    if lang in supported_languages:
        change_json_value(parse_path("full_path.project", "path.basic_info.json"), "language", lang)
        log("INFO", "change_language")

def execute_arg_parse() -> None:
    try:
        parse_objects_task(parse_path("full_path.project", "path.documents.json"))
    except FileNotFoundError:
        log("ERROR", "file_parsing.no_file.error")

def execute_arg_parse_parlamint() -> None:
    try:
        parse_parlamint_objects_task(open_shelve("main"))
    except FileNotFoundError:
        log("ERROR", "file_parsing.no_file.error")

"""def execute_arg_random(params):
    target_path, json_file = parse_directory(PROJECT, DIRECTORY_LIB, params[0]), \
                             parse_directory(PROJECT, RESOURCES, params[1])
    try:
        os.mkdir(target_path)
    except OSError:
        print("already exists")
    finally:
        for random_file in parse_json(json_file)["random files"]:
            archive_path = parse_directory(PROJECT, DOCUMENTS, f"{add_pdf_to_path(random_file['path'])}")
            meeting_text = retrieve_text_task(archive_path, random_file["page"])
            write_text(parse_directory(target_path, add_txt_to_name(random_file["full name"])), meeting_text)"""

# MAIN
def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--cer", nargs="+", help="get character error rate based on directories")
    parser.add_argument("-l", "--lang", type=str, help="change language of logs")
    parser.add_argument("-f", "--find", nargs="+", help="search for parsed object")
    parser.add_argument("-p", "--parse", nargs="*", help="parse files for shelving [serialization]")
    # parser.add_argument("-pp", "--parse_parlamint", nargs="*")
    # parser.add_argument("-wp", "--write_parlamint", nargs="*")
    parser.add_argument("-r", "--random", nargs="+", help="get text for randomly chosen files")

    args = parser.parse_args()

    if args.cer:
        print(f"Average: {execute_arg_cer(args.cer)}%")

    if args.lang:
        execute_arg_language(args.lang)

    if args.find:
        try:
            for found_object in execute_arg_find(args.find):
                print(found_object)
        except TypeError:
            print("TypeError reached")

    if args.parse is not None:
        execute_arg_parse()

    """if args.random:
        execute_arg_random(args.random)"""

"""def save_xml_file(xml_document: ET, target_path: str) -> None:
    tree = ET.ElementTree(xml_document)
    ET.indent(tree, space="    ")
    tree.write(target_path, encoding="UTF-8", xml_declaration=True)"""

if __name__ == "__main__":
    log("INFO", "main_program.start")
    main()
    log("INFO", "main_program.end")

    # file = execute_arg_find(["file", "year", "1919"])
    # file = execute_arg_find(["file", "name", "7_XXIV_SKJ_redni_14.4.1932"])
    # file = execute_arg_find(["file", "name", "8_XXV_SKJ_redni_15.4.1932"])
    file = execute_arg_find(["file", "name", "9_XXVI_SKJ_redni_15.4.1932"])

    parlamint_document, attendees = parse_parlamint_objects_task([file[0]], [])
    create_parlamint_xml_document(parlamint_document, "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/test3.xml")

    """xml = docx.print_xml()
    save_xml_file(xml, "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/test.xml")"""

    """y = DocxDocument(x)
    z = y.print_xml()"""

    # save_xml_file(y, "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma")
