# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main.py

import argparse

from code import FileParsingTask


def main():
    data = FileParsingTask("/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/library/datoteke.json")

    for file in data.get_files():
        print(file)

if __name__ == "__main__":
    main()