# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main.py

import argparse

import locale
import ResourceBundle

from src import FileParsingTask, FindObjectsTask

INFO_DATOTEKE = "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/lib/datoteke.json"

def execute_find(obj):
    params = input("Parametri: ")
    find_task = FindObjectsTask(data, obj, params.split(" ")).get_candidates()

    for file in find_task:
        print(file)


def main():

    parser = argparse.ArgumentParser()
    # parser.add_argument("--parse", metavar="file_or_dir", type=str, help="parse .json file to get object")

    parser.add_argument("-f", "--find", help="search for parsed object")
    args = parser.parse_args()

    if args.find is not None:
        execute_find(args.find)

if __name__ == "__main__":
    data = FileParsingTask(INFO_DATOTEKE)
    # execute_find("file")
    # main()
    bundle = ResourceBundle.get_bundle("program_messages", locale.getlocale())
    everything = dict(bundle)
    while bundle.parent is not None:
        bundle = bundle.parent
        everything.update(dict(bundle))
