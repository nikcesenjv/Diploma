# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_titles.py

from .translations import MEETINGS

from src.objects.general_objects import File

def parlamint_main_title_sl(file: File) -> str:
    return f"Parlamentarni korpus ParlaMint, {file.meeting} {file.num_arab} [ParlaMint]"

def parlamint_main_title_en(file: File) -> str:
    return f"Parliamentary corpus ParlaMint, {MEETINGS[file.meeting]} {file.num_arab} [ParlaMint]"

def parlamint_sub_title_sl(file: File) -> str:
    return f"Zapisi sej {file.assembly}, indeks {file.index}, {file.date}"

def parlaming_sub_title_en(file: File) -> str:
    return f"Minutes of the {file.assembly}, index {file.index}, {file.date}"
