# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main.py

import argparse

from src import FileParsingTask, FindObjectsTask
from src import LoggingTask as Log

PARSING_JSON = "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/lib/datoteke.json"

MAIN_PROGRAM_END = "main_program.end"

# TODO: RAZLIČNI JEZIKI, SPLETNA STRAN, XML

def execute_find(params):
    for obj in FindObjectsTask(data, params).get_candidates():
        print(obj)


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("--parse", metavar="file_or_dir", type=str, help="parse .json file to get object")

    parser.add_argument("-f", "--find", nargs="+", help="search for parsed object")
    parser.add_argument("-l", "--lang", type=str, help="change language of logs")
    parser.add_argument("-t", "--text", nargs="+", help="convert pdf file to text")
    args = parser.parse_args()

    if args.find is not None:
        execute_find(args.find)

if __name__ == "__main__":
    data = FileParsingTask(PARSING_JSON)
    main()

    Log("INFO", MAIN_PROGRAM_END)
