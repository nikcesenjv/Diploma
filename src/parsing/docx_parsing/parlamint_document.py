# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_document.py

from docx_document import DocxDocument
from src.parsing import File

class ParlamintDocument:
    def __init__(self, file, docx_document):
        self._file: File = file
        self._docx_document: DocxDocument = docx_document

        self._xml: str = None

    @property
    def file(self) -> File:
        return self._file

    @file.setter
    def file(self, new_file: File) -> None:
        self._file = new_file

    @property
    def docx_document(self) -> DocxDocument:
        return self._docx_document

    @docx_document.setter
    def docx_document(self, new_docx_document: DocxDocument) -> None:
        self._docx_document = new_docx_document

    def add_head_info(self) -> None:
        ...