# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_document.py

from src.objects.docx_objects import DocxDocument
from src.objects.general_objects import File

class ParlamintDocument:
    def __init__(self, file, docx_document, original_text=True):
        self._file: File = file
        self._docx_document: DocxDocument = docx_document

        self._original_text: bool = original_text

    # GETTERS & SETTERS
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

    @property
    def original_text(self) -> bool:
        return self._original_text

    @original_text.setter
    def original_text(self, boolean_change: bool):
        self._original_text = boolean_change
