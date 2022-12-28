# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main.py

import argparse

from src import ConvertNumeralsTask, FileParsingTask


def execute_find(obj):
    match obj:
        case "main":
            print("main")
        case "inner":
            print("inner")
        case "file":
            print("file")
        case _:
            print("type of object not found")
    print(data)


def main():


    parser = argparse.ArgumentParser()
    # parser.add_argument("--parse", metavar="file_or_dir", type=str, help="parse .json file to get object")

    parser.add_argument("-f", "--find", help="search for parsed object")
    args = parser.parse_args()

    if args.find is not None:
        execute_find(args.find)

if __name__ == "__main__":
    data = FileParsingTask("/lib/datoteke.json")

    main()