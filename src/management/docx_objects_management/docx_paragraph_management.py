# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_paragraph_management.py

from src.objects.docx_objects import DocxParagraph

def split_docx_paragraph(paragraph: DocxParagraph):
    ...

def docx_paragraphs_to_string(paragraphs: list[DocxParagraph]):
    return "".join([paragraph.text for paragraph in paragraphs])
