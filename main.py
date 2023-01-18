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
from src.retrieve_resources import parse_json

# DIRECTORIES
PROJECT = "full_path.project"
DOCUMENTS = "path.documents.json"
DOCUMENTS_PDF = "path.documents.pdf"
# TEST_FILES = "path.test_files"
LIB = "path.lib"
RESOURCES = "path.src.resources"

# MESSAGES [INFO]
MAIN_PROGRAM_START = "main_program.start"
MAIN_PROGRAM_END = "main_program.end"

# MESSAGES [ERROR]
FIND_INDEX_ERROR = "find_objects.index.error"
PARSE_FILE_ERROR = "file_parsing.no_file.error"

def execute_arg_find(params):
    try:
        return find_objects_task(open_pickle(), params)
    except IndexError:
        log("ERROR", FIND_INDEX_ERROR)

def execute_arg_language():
    pass

def execute_arg_parse():
    try:
        with open("parsed_objects.pickle", "wb") as file:
            pickle.dump(file_parsing_task(retrieve_directory_task(PROJECT, DOCUMENTS)), file)
    except FileNotFoundError:
        log("ERROR", PARSE_FILE_ERROR)

def execute_arg_random(params):
    target_path, json_file = retrieve_directory_task(PROJECT, LIB, params[0]), \
                             retrieve_directory_task(PROJECT, RESOURCES, params[1])
    try:
        os.mkdir(target_path)
    except OSError:
        print("already exists")
    finally:
        for random_file in parse_json(json_file)["random files"]:
            file_path = execute_arg_find(["file", "name", random_file["full name"]])[0].get_path()
            pdf_path = retrieve_directory_task(PROJECT, DOCUMENTS_PDF, file_path) + ".pdf"
            text = archive_to_text_task(pdf_path, random_file["page"])
            write_text(retrieve_directory_task(target_path, random_file["full name"]) + ".txt", text)

def open_pickle():
    with open("parsed_objects.pickle", "rb") as file:
        return pickle.load(file)

def write_text(full_path, text):
    with open(full_path, "w") as file:
        file.write(text)

# EXECUTE METHODS
"""def execute_arg_cer(params):
    # return retrieve_cer_task(params[0], params[1])
    try:
        cer_scores = []
        full_directory = retrieve_directory_task(PROJECT, TEST_FILES, params[0])
        for file in os.listdir(full_directory):
            full_path_first = full_directory + f"/{file}"
            full_path_second = full_path_first.replace(params[0], params[1])
            cer_scores.append(retrieve_cer_task(full_path_first, full_path_second))
        print(sum(cer_scores) / len(cer_scores))
    except FileNotFoundError:
        print("file not found error")

def execute_arg_random(params):
    # path, pages = params[0], [int(page) for page in params[1:]]
    # print(archive_to_text_task(retrieve_directory_task(PROJECT, DOCUMENTS_PDF) + path + ".pdf", pages))
    try:
        # os.mkdir(retrieve_directory_task(PROJECT, LIB, params[0]))
        data = parse_json(retrieve_directory_task(PROJECT, RESOURCES, params[1]))
        for k in data["random files"]:
            print(k)
        # data = parse_json("/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/src/resources/test_files_cer.json")
    except OSError:
        print("already exists")
    # data = parse_json(retrieve_directory_task(PROJECT, RESOURCES, params[1]))
    folder_path = retrieve_directory_task(PROJECT, LIB, params[0])
    for random_meeting in parse_json(retrieve_directory_task(PROJECT, RESOURCES, params[1]))["random files"]:
        if random_meeting["full name"] == "1_XXI_SKJ_redni_18.6.1934":
            random_meeting_path = execute_arg_find(["file", "name", random_meeting["full name"]])[0]
            print(random_meeting_path)
            # print(retrieve_directory_task(PROJECT, DOCUMENTS_PDF, random_meeting_path) + ".pdf")
            # text = archive_to_text_task(retrieve_directory_task(PROJECT, DOCUMENTS, random_meeting_path) + ".pdf", random_meeting["page"])
            # write_text(folder_path, random_meeting["full name"] + ".txt", text)

def execute_arg_random(params):
    try:
        full_path = retrieve_directory_task(PROJECT, LIB, params[0])
        # os.mkdir(retrieve_directory_task(PROJECT, LIB, params[0]))
        # data = parse_json(retrieve_directory_task(PROJECT, RESOURCES, params[1]))
        for k in parse_json(retrieve_directory_task(PROJECT, RESOURCES, params[1]))["random files"]:
            if k["full name"] == "1_XXI_SKJ_redni_18.6.1934":
                # path = retrieve_directory_task(full_path, k.get_path())
                # print(path)
                random_meeting = execute_arg_find(["file", "name", k["full name"]])[0].get_path()
                path = retrieve_directory_task(full_path, random_meeting)
                print(k["page"])
    except OSError:
        print("already exists")

def execute_arg_text():
    pass

# PICKLE
def open_pickle():
    with open("parsed_objects.pickle", "rb") as file:
        return pickle.load(file)

def write_text(path, title, text):
    with open(path + title, "w") as file:
        file.write(text)"""

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--cer", nargs="+", help="get character error rate based on directories")
    parser.add_argument("-f", "--find", nargs="+", help="search for parsed object")
    parser.add_argument("-p", "--parse", nargs="*", help="parse files into pickle file")
    parser.add_argument("-r", "--random", nargs="+", help="get text for randomly chosen files")
    args = parser.parse_args()

    """if args.cer:
        execute_arg_cer(args.cer)"""

    if args.find:
        for found_object in execute_arg_find(args.find):
            print(found_object)

    if args.parse is not None:
        execute_arg_parse()

    """if args.random:
        execute_arg_random(args.random)"""

    """parser.add_argument("-c", "--cer", nargs="+", help="get character error rate based on directories")
    parser.add_argument("-l", "--lang", type=str, help="change language of logs")
    parser.add_argument("-t", "--text", nargs="+", help="convert pdf file to text")
    """

if __name__ == "__main__":
    execute_arg_random(["test_files_cer/new_ocr", "test_files_cer.json"])
    log("INFO", MAIN_PROGRAM_START)
    main()
    log("INFO", MAIN_PROGRAM_END)

    # print(open_pickle())
