# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main.py

import argparse
import os
import shelve

import time

from src import *
from src.logging import log
from src.parsing import *

# DIRECTORIES
PROJECT = "full_path.project"
DOCUMENTS = "path.documents"
DOCUMENTS_JSON = "path.documents.json"
DIRECTORY_LIB = "path.lib"
RESOURCES = "path.src.resources"
BASIC_INFO = "path.basic_info.json"

# EXECUTE METHODS
def execute_arg_cer(params):
    try:
        first_path, second_path = parse_directory(PROJECT, DIRECTORY_LIB, params[0]), \
                                  parse_directory(PROJECT, DIRECTORY_LIB, params[1])

        return [retrieve_cer_task(parse_directory(first_path, first_file),
                                  parse_directory(second_path, second_file))
                                  for first_file, second_file in
                                  zip(sorted(os.listdir(first_path)), sorted(os.listdir(second_path)))]
    except FileNotFoundError:
        log("ERROR", "find_objects.index.error")
        return []

def execute_arg_find(params):
    try:
        # return find_objects_task(open_pickle(), params)
        return find_objects_task(open_shelve(params[0]), params)
    except IndexError:
        log("ERROR", "find_objects.index.error")
        return []

def execute_arg_language(lang):
    supported_languages = ["sl", "en"]
    if lang in supported_languages:
        change_json_value(parse_directory(PROJECT, BASIC_INFO), "language", lang)
        log("INFO", "change_language")

def execute_arg_parse():
    try:
        with shelve.open("testDB") as db:
            db["file"], db["inner"], db["main"] = file_parsing_task(parse_directory(PROJECT, DOCUMENTS_JSON))

    except FileNotFoundError:
        log("ERROR", "file_parsing.no_file.error")

def execute_arg_random(params):
    target_path, json_file = parse_directory(PROJECT, DIRECTORY_LIB, params[0]), \
                             parse_directory(PROJECT, RESOURCES, params[1])
    try:
        os.mkdir(target_path)
    except OSError:
        print("already exists")
    finally:
        for random_file in parse_json(json_file)["random files"]:
            archive_path = parse_directory(PROJECT, DOCUMENTS, f"{add_pdf_to_path(random_file['path'])}")
            meeting_text = archive_to_text_task(archive_path, random_file["page"])
            write_text(parse_directory(target_path, add_txt_to_name(random_file["full name"])), meeting_text)

# HELPING METHODS
def open_shelve(type_of_object):
    with shelve.open("testDB") as db:
        return db[type_of_object]

def write_text(full_path, text):
    with open(full_path, "w") as f:
        f.write(text)

def calculate_average(cer_scores):
    return round(sum(cer_scores) / len(cer_scores) * 100, 2)

# MAIN
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--cer", nargs="+", help="get character error rate based on directories")
    parser.add_argument("-l", "--lang", type=str, help="change language of logs")
    parser.add_argument("-f", "--find", nargs="+", help="search for parsed object")
    parser.add_argument("-p", "--parse", nargs="*", help="parse files for shelving [serialization]")
    parser.add_argument("-r", "--random", nargs="+", help="get text for randomly chosen files")

    # TODO: XML PARSER

    args = parser.parse_args()

    if args.cer:
        try:
            print(f"Average: {(calculate_average(execute_arg_cer(args.cer)))}%")
        except TypeError:
            print("not found")

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

    if args.random:
        execute_arg_random(args.random)

if __name__ == "__main__":
    # log("INFO", "main_program.start")
    # main()
    # log("INFO", "main_program.end")
    start = time.time()
    # x = execute_arg_find(["file", "name", "1_V_ZNPSHS_redni_22.3.1919"])
    x = execute_arg_find(["file", "year", "1919"])
    for _file in x:
        print(_file)
    end = time.time()

    print(end - start)
    # open_shelve()
    # execute_arg_parse_pickle()
