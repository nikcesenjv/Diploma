from src.objects.general_objects import File

from .translations import MEETINGS

def xml_meeting_type(file: File) -> tuple[str, str]:
    return file.meeting.capitalize(), xml_meeting_type_ana(file)

def xml_meeting_type_ana(file: File) -> str:
    return f"#parla.lower #parla.meeting.{MEETINGS[file.meeting]}"

def xml_meeting_num(file: File) -> tuple[str, str]:
    return f"Indeks {file.index}", xml_meeting_num_ana(file)

def xml_meeting_num_ana(file: File) -> str:
    return f"#parla.lower #parla.term #{file.assembly}.{file.index}"
