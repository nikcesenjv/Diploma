# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main.py

import argparse
import pickle

from src import archive_to_text_task, file_parsing_task, find_objects_task, retrieve_directory_task
from src.logging import log

# DIRECTORIES
DIPLOMA = "full_path.diploma"
DOCUMENTS = "path.documents.json"
DOCUMENTS_PDF = "path.documents.pdf"

# MESSAGES [INFO]
MAIN_PROGRAM_START = "main_program.start"
MAIN_PROGRAM_END = "main_program.end"

# MESSAGES [ERROR]
FIND_INDEX_ERROR = "find_objects.index.error"
PARSE_FILE_ERROR = "file_parsing.no_file.error"

# EXECUTE METHODS
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

    parser.add_argument("-f", "--find", nargs="+", help="search for parsed object")
    parser.add_argument("-p", "--parse", nargs="*", help="parse files into pickle file")
    parser.add_argument("-r", "--random", nargs="+", help="get text for randomly chosen files")
    args = parser.parse_args()

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
