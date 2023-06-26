# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_attendee.py

from src.management.text_management import capitalize_every_word

class ParlamintAttendee:
    def __init__(self, name: str, attendee_role: str = "chair"):
        self._name: str = capitalize_every_word(name)
        self._attendee_role: str = attendee_role

        """self.parse_name()
        self.name = capitalize_every_word(self.name)"""

        self._id: str = self.generate_id()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = capitalize_every_word(new_name)
        self.id = self.generate_id()

    def parse_name(self) -> str:
        if self.name[-1] == ".":
            self.name = self.name[:-1]
        self.id = self.generate_id()

        """if is_any_close_match(self.name, "izvestilac"):
            self.name = self.name.replace(f"{remove_close_matches(self.name.lower(), 'izvestilac')[0] }", "")
            self.name = capitalize_every_word(self.name)
            self.attendee_role = "reporter"""

    @property
    def attendee_role(self) -> str:
        return self._attendee_role

    @attendee_role.setter
    def attendee_role(self, new_attendee_role: str) -> None:
        self._attendee_role = new_attendee_role

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id: str) -> None:
        self._id = new_id
        
    def generate_id(self):
        parsed_name = [name_part for name_part in self.name.split(" ") if "." not in name_part]
        return f"#{''.join(parsed_name[1:] + [parsed_name[0]])}".replace(".", "")
