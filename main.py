# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main.py

import argparse
import pickle

from src import FileParsingTask, FindObjectsTask, RetrieveDirectoryTask
from src import LoggingTask as Log

# DIRECTORIES
DIPLOMA = "full_path.diploma"
DOCUMENTS = "path.documents.json"

# MESSAGES
FIND_INDEX_ERROR = "find_objects.params.error"
MAIN_PROGRAM_START = "main_program.start"
MAIN_PROGRAM_END = "main_program.end"
PARSE_PICKLE = "pickle.success"

# EXECUTE METHODS
def execute_arg_find(params):
    try:
        for obj in FindObjectsTask(open_pickle(), params).get_candidates():
            print(obj)
    except IndexError:
        Log("ERROR", FIND_INDEX_ERROR)

def execute_arg_language():
    pass

def execute_arg_parse():
    with open("parsed_documents.pickle", "wb") as file:
        pickle.dump(FileParsingTask(RetrieveDirectoryTask(DIPLOMA, DOCUMENTS).retrieve_directory_content()), file)

    Log("INFO", PARSE_PICKLE, "parsed_documents.pickle")

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
    parser.add_argument("-l", "--lang", type=str, help="change language of logs")
    parser.add_argument("-p", "--parse", nargs="*", help="parse files into pickle file")
    parser.add_argument("-t", "--text", nargs="+", help="convert pdf file to text")
    args = parser.parse_args()

    if args.find:
        execute_arg_find(args.find)

    if args.parse is not None:
        execute_arg_parse()

if __name__ == "__main__":
    Log("INFO", MAIN_PROGRAM_START)
    main()
    Log("INFO", MAIN_PROGRAM_END)
