# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_parsing_task.py

from src.parsing import DocxDocument

def docx_parsing_task(path: str, convert_to_xml: bool = False) -> DocxDocument | None:
    document = DocxDocument(path)

    if not convert_to_xml:
        return document

    
