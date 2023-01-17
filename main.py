# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main.py

import argparse
import os
import pickle

from src import archive_to_text_task
from src import file_parsing_task
from src import find_objects_task
from src import retrieve_directory_task
from src import retrieve_cer_task
from src.logging import log

# DIRECTORIES
DIPLOMA = "full_path.diploma"
DOCUMENTS = "path.documents.json"
DOCUMENTS_PDF = "path.documents.pdf"
TEST_FILES = "path.test_files"

# MESSAGES [INFO]
MAIN_PROGRAM_START = "main_program.start"
MAIN_PROGRAM_END = "main_program.end"

# MESSAGES [ERROR]
FIND_INDEX_ERROR = "find_objects.index.error"
PARSE_FILE_ERROR = "file_parsing.no_file.error"

# EXECUTE METHODS
def execute_arg_cer(params):
    # return retrieve_cer_task(params[0], params[1])
    try:
        cer_scores = []
        full_directory = retrieve_directory_task(DIPLOMA, TEST_FILES, params[0])
        for file in os.listdir(full_directory):
            full_path_first = full_directory + f"/{file}"
            full_path_second = full_path_first.replace(params[0], params[1])
            cer_scores.append(retrieve_cer_task(full_path_first, full_path_second))
        print(sum(cer_scores) / len(cer_scores))
    except FileNotFoundError:
        print("file not found error")

def execute_arg_find(params):
    try:
        found_objects = find_objects_task(open_pickle(), params)
        for found_object in found_objects:
            print(found_object)
        return found_objects
    except IndexError:
        log("ERROR", FIND_INDEX_ERROR)

def execute_arg_language():
    pass

def execute_arg_parse():
    try:
        with open("parsed_documents.pickle", "wb") as file:
            pickle.dump(file_parsing_task(retrieve_directory_task(DIPLOMA, DOCUMENTS)), file)
    except FileNotFoundError:
        log("ERROR", PARSE_FILE_ERROR)

def execute_arg_random(params):
    path, pages = params[0], [int(page) for page in params[1:]]
    print(archive_to_text_task(retrieve_directory_task(DIPLOMA, DOCUMENTS_PDF) + path + ".pdf", pages))

def execute_arg_text():
    pass

# PICKLE
def open_pickle():
    with open("parsed_documents.pickle", "rb") as file:
        return pickle.load(file)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--cer", nargs="+", help="get character error rate based on directories")
    parser.add_argument("-f", "--find", nargs="+", help="search for parsed object")
    parser.add_argument("-p", "--parse", nargs="*", help="parse files into pickle file")
    parser.add_argument("-r", "--random", nargs="+", help="get text for randomly chosen files")
    args = parser.parse_args()

    if args.cer:
        execute_arg_cer(args.cer)

    if args.find:
        execute_arg_find(args.find)

    if args.parse is not None:
        execute_arg_parse()

    if args.random:
        execute_arg_random(args.random)

    """parser.add_argument("-c", "--cer", nargs="+", help="get character error rate based on directories")
    parser.add_argument("-l", "--lang", type=str, help="change language of logs")
    parser.add_argument("-t", "--text", nargs="+", help="convert pdf file to text")
    """

if __name__ == "__main__":
    log("INFO", MAIN_PROGRAM_START)
    main()
    log("INFO", MAIN_PROGRAM_END)
