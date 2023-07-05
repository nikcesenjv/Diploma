# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_attendee_management.py

from src.management.text_management import is_close_match_attendee, only_letters, remove_close_matches, \
    has_similar_string

from src.objects.parlamint_objects import ParlamintAttendee

def is_attendee(name: str, attendees: list[ParlamintAttendee]) -> bool:
    for attendee in attendees:
        if is_close_match_attendee(name, attendee.name):
            check_attendee_name(name, attendee)
            # TODO: check attendee role
            return True
    return False

def find_attendee(name: str, attendees: list[ParlamintAttendee]) -> ParlamintAttendee:
    for attendee in attendees:
        if is_close_match_attendee(name, attendee.name):
            # check_attendee_name(name, attendee)
            return attendee

def check_attendee_name(string: str, attendee: ParlamintAttendee) -> ParlamintAttendee:
    if not only_letters(attendee.name):
        attendee.name = string

def create_parlamint_attendee(attendee_name: str, attendee_role: str = None) -> ParlamintAttendee:
    if attendee_role == "chair":
        return create_parlamint_attendee_chair(attendee_name)

    return create_parlamint_attendee_regular(attendee_name)

def create_parlamint_attendee_chair(attendee_name: str, attendee_role: str = "chair") -> ParlamintAttendee:
    similar_words = ["pretsednik", "sekretar", "dr"]
    return ParlamintAttendee(remove_close_matches(attendee_name, similar_words), attendee_role)

def create_parlamint_attendee_regular(attendee_name: str, attendee_role: str = "regular") -> ParlamintAttendee:
    similar_words = ["ministar"]
    return ParlamintAttendee(remove_close_matches(attendee_name, similar_words), attendee_role)

def create_parlamint_attendee_reporter(attendee_name: str, attendee_role: str = "reporter") -> ParlamintAttendee:
    similar_words = ["izvestilac", "dr"]
    return ParlamintAttendee(remove_close_matches(attendee_name, similar_words), attendee_role)
