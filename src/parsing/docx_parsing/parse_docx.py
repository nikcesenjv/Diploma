# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parse_docx.py

from docx_document import DocxDocument

def parse_docx(path):
    docx_document = DocxDocument(path)
    for paragraph in docx_document.paragraphs:
        print(paragraph.text_with_bold_property)

parse_docx("/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/lib/documents/word/19_1932_SKJ/18-40_redni/7_XXIV_SKJ_redni_14.4.1932.docx")
