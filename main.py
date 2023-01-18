# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main.py

import argparse
import os
import pickle

from src import *
from src.logging import log
from src.parsing import parse_directory, parse_json, change_json_value

# DIRECTORIES
PROJECT = "full_path.project"
DOCUMENTS_JSON = "path.documents.json"
DOCUMENTS_PDF = "path.documents.pdf"
DIRECTORY_LIB = "path.lib"
RESOURCES = "path.src.resources"
BASIC_INFO = "path.basic_info.json"

# MESSAGES [INFO]
MAIN_PROGRAM_START = "main_program.start"
MAIN_PROGRAM_END = "main_program.end"

# MESSAGES [ERROR]
FIND_INDEX_ERROR = "find_objects.index.error"
NO_FILE_ERROR = "file_parsing.no_file.error"

# EXECUTE METHODS
def execute_arg_cer(params):
    try:
        first_path, second_path = parse_directory(PROJECT, DIRECTORY_LIB, params[0]), \
                                  parse_directory(PROJECT, DIRECTORY_LIB, params[1])

        return [retrieve_cer_task(parse_directory(first_path, first_file),
                                  parse_directory(second_path, second_file))
                                  for first_file, second_file in zip(sorted(os.listdir(first_path)),
                                                                     sorted(os.listdir(second_path)))]
    except FileNotFoundError:
        log("ERROR", NO_FILE_ERROR)

def execute_arg_find(params):
    try:
        return find_objects_task(open_pickle(), params)
    except IndexError:
        log("ERROR", FIND_INDEX_ERROR)

def execute_arg_language(lang):
    change_json_value(parse_directory(PROJECT, BASIC_INFO), "language", lang)

def execute_arg_parse():
    try:
        with open("parsed_objects.pickle", "wb") as file:
            pickle.dump(file_parsing_task(parse_directory(PROJECT, DOCUMENTS_JSON)), file)
    except FileNotFoundError:
        log("ERROR", NO_FILE_ERROR)

def execute_arg_random(params):
    target_path, json_file = parse_directory(PROJECT, DIRECTORY_LIB, params[0]), \
                             parse_directory(PROJECT, RESOURCES, params[1])
    try:
        os.mkdir(target_path)
    except OSError:
        print("already exists")
    finally:
        for random_file in parse_json(json_file)["random files"]:
            archive_path = parse_directory(PROJECT, DOCUMENTS_PDF, f"{random_file['path']}.pdf")
            meeting_text = archive_to_text_task(archive_path, random_file["page"])
            write_text(parse_directory(target_path, f"{random_file['full name']}.txt"), meeting_text)

# HELPING METHODS
def open_pickle():
    with open("parsed_objects.pickle", "rb") as file:
        return pickle.load(file)

def write_text(full_path, text):
    with open(full_path, "w") as file:
        file.write(text)

def calculate_average(cer_scores):
    return sum(cer_scores) / len(cer_scores)

# MAIN
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--cer", nargs="+", help="get character error rate based on directories")
    parser.add_argument("-l", "--lang", type=str, help="change language of logs")
    parser.add_argument("-f", "--find", nargs="+", help="search for parsed object")
    parser.add_argument("-p", "--parse", nargs="*", help="parse files into pickle file")
    parser.add_argument("-r", "--random", nargs="+", help="get text for randomly chosen files")
    args = parser.parse_args()

    if args.cer:
        cer_scores = execute_arg_cer(args.cer)
        print(f"Average: {calculate_average(cer_scores)}")

    if args.lang:
        execute_arg_language(args.lang)

    if args.find:
        for found_object in execute_arg_find(args.find):
            print(found_object)

    if args.parse is not None:
        execute_arg_parse()

    if args.random:
        execute_arg_random(args.random)

    """parser.add_argument("-c", "--cer", nargs="+", help="get character error rate based on directories")
    parser.add_argument("-t", "--text", nargs="+", help="convert pdf file to text")
    """

if __name__ == "__main__":
    log("INFO", MAIN_PROGRAM_START)
    main()
    log("INFO", MAIN_PROGRAM_END)
