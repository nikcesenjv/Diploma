# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_attendee.py

class ParlamintAttendee:
    def __init__(self, name: str, attendee_type: str):
        self._name: str = name
        self._attendee_type: str = attendee_type
        
        self._id: str = self.create_id()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def attendee_type(self) -> str:
        return self._attendee_type

    @attendee_type.setter
    def attendee_type(self, new_attendee_type: str) -> None:
        self._attendee_type = new_attendee_type

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id: str) -> None:
        self._id = new_id
        
    def create_id(self):
        parsed_name = self.name.split(" ")
        return f"#{''.join(parsed_name[1:] + [parsed_name[0]])}"
