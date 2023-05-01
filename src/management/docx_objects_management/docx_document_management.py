# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_document_management.py

import xml.etree.ElementTree as ET

from zipfile import ZipFile

from src.management.path_management import parse_path

from src.objects.docx_objects import DocxParagraph
from src.objects.general_objects import File

def document_paragraphs(file: File, namespace: dict[str, str]) -> list[DocxParagraph]:
    document = ET.fromstring(ZipFile(parse_path("full_path.documents", file.word_path)).read("word/document.xml"))
    return document.find("w:body", namespace).findall("w:p", namespace)
