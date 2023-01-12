# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main.py

import argparse
import pickle

# from src import FileParsingTask, FindObjectsTask, RetrieveDirectoryTask
from src import file_parsing_task
from src import find_objects_task
from src import retrieve_directory_task
from src import log

# DIRECTORIES
DIPLOMA = "full_path.diploma"
DOCUMENTS = "path.documents.json"
DOCUMENTS_PDF = "path.documents.pdf"

# MESSAGES
FIND_INDEX_ERROR = "find_objects.params.error"
MAIN_PROGRAM_START = "main_program.start"
MAIN_PROGRAM_END = "main_program.end"
PARSE_PICKLE = "pickle.success"

# EXECUTE METHODS
def execute_arg_find(params):
    try:
        for found_object in find_objects_task(open_pickle(), params):
            print(found_object)
    except IndexError:
        log("ERROR", FIND_INDEX_ERROR)

def execute_arg_language():
    pass

def execute_arg_parse():
    with open("parsed_documents.pickle", "wb") as file:
        pickle.dump(file_parsing_task(retrieve_directory_task(DIPLOMA, DOCUMENTS)), file)


"""def execute_arg_find(params):
    try:
        return FindObjectsTask(open_pickle(), params).get_candidates()
    except IndexError:
        log("ERROR", FIND_INDEX_ERROR)

def execute_arg_language():
    pass

def execute_arg_parse():
    with open("parsed_documents.pickle", "wb") as file:
        pickle.dump(FileParsingTask(RetrieveDirectoryTask(DIPLOMA, DOCUMENTS).retrieve_directory_content()), file)

    # Log("INFO", PARSE_PICKLE, "parsed_documents.pickle")
    print("error")

def execute_arg_text():
    pass"""

"""def execute_arg_random(file_name):
    data = execute_arg_find(["file", "name", file_name])[0].get_path()
    path = RetrieveDirectoryTask(DIPLOMA, DOCUMENTS_PDF).retrieve_directory_content() + data + ".pdf"
    text = ArchiveToTextTask(path).get_content(1, 1)
    print(text)"""

# PICKLE
def open_pickle():
    with open("parsed_documents.pickle", "rb") as file:
        return pickle.load(file)

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-f", "--find", nargs="+", help="search for parsed object")
    parser.add_argument("-p", "--parse", nargs="*", help="parse files into pickle file")
    parser.add_argument("-r", "--random", help="get text for randomly chosen files")
    args = parser.parse_args()

    """if args.find:
        try:
            for obj in execute_arg_find(args.find):
                print(obj)
        except IndexError:
            log("ERROR", FIND_INDEX_ERROR)"""

    if args.find:
        execute_arg_find(args.find)

    if args.parse is not None:
        execute_arg_parse()

    """if args.find:
        for obj in execute_arg_find(args.find):
            print(obj)

    if args.parse is not None:
        execute_arg_parse()

    if args.random:
        execute_arg_random(args.random)"""

    """parser.add_argument("-c", "--cer", nargs="+", help="get character error rate based on directories")
    parser.add_argument("-l", "--lang", type=str, help="change language of logs")
    parser.add_argument("-t", "--text", nargs="+", help="convert pdf file to text")
    """

if __name__ == "__main__":
    log("INFO", MAIN_PROGRAM_START)
    main()
    log("INFO", MAIN_PROGRAM_END)
