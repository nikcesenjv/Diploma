# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka structure.py

class Structure:
    def __init__(self, name: str, path: str):
        self._name: str = name
        self._path: str = path

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, new_path: str) -> None:
        self._path = new_path
