# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka main_folder.py

from .structure import Structure

from ..general_objects import InnerFolder

class MainFolder(Structure):
    def __init__(self, name, path):
        super().__init__(name, path)

        self._index, self._year, self._assembly = self.parse_name()

        self._folders: list[InnerFolder] = []

    # PRINT OBJECT
    def __str__(self):
        return f"Ime mape:     {self.name}\n" \
               f"Indeks:       {self.index}\n" \
               f"Leto:         {self.year}\n" \
               f"Organizacija: {self.assembly}\n"

    # PARSING METHOD
    def parse_name(self) -> tuple[int, str, str]:
        parsed = self.name.split("_")
        return int(parsed[0]), parsed[1], parsed[2]

    # GETTERS & SETTERS
    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, new_index: int) -> None:
        self._index = new_index

    @property
    def year(self) -> str:
        return self._year

    @year.setter
    def year(self, new_year: int | str) -> None:
        if type(new_year) == int:
            self._year = str(new_year)
        else:
            self._year = new_year

    @property
    def assembly(self) -> str:
        return self._assembly

    @assembly.setter
    def assembly(self, new_assembly: str) -> None:
        self._assembly = new_assembly

    @property
    def folders(self) -> list[InnerFolder]:
        return self._folders

    @folders.setter
    def folders(self, new_list: list[InnerFolder]) -> None:
        self._folders = new_list

    def add_folder(self, new_folder: InnerFolder) -> None:
        self._folders.append(new_folder)

    def add_folders(self, new_folders: list[InnerFolder]) -> None:
        self._folders += new_folders
