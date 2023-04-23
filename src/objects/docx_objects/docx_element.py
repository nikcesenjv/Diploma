# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_element.py

from src.objects.docx_objects import DocxParagraph

class DocxElement:
    def __init__(self, element_type: str, docx_paragraphs: list[DocxParagraph]):
        self._element_type: str = element_type
        self._docx_paragraphs: list[DocxParagraph] = docx_paragraphs

    @property
    def element_type(self) -> str:
        return self._element_type

    @element_type.setter
    def element_type(self, new_element_type: str) -> None:
        self._element_type = new_element_type

    @property
    def docx_paragraphs(self) -> list[DocxParagraph]:
        return self._docx_paragraphs

    @docx_paragraphs.setter
    def docx_paragraphs(self, new_docx_paragraphs: list[DocxParagraph]) -> None:
        self._docx_paragraphs = new_docx_paragraphs
