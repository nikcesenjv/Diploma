from .translations import MEETINGS

from src.objects.general_objects import File

def parlamint_meeting_type(file: File) -> tuple[str, str]:
    return file.meeting.capitalize(), parlamint_meeting_type_ana(file)

def parlamint_meeting_type_ana(file: File) -> str:
    return f"#parla.lower #parla.meeting.{MEETINGS[file.meeting]}"

def parlamint_meeting_num(file: File) -> tuple[str, str]:
    return f"Indeks {file.index}", parlamint_meeting_num_ana(file)

def parlamint_meeting_num_ana(file: File) -> str:
    return f"#parla.lower #parla.term #{file.assembly}.{file.index}"
