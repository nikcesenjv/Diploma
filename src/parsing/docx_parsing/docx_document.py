# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_document.py

import xml.etree.ElementTree as ET

from zipfile import ZipFile

from docx_paragraph import DocxParagraph
from namespace import Namespace

class DocxDocument(Namespace):
    def __init__(self, path: str):
        self._path: str = path

        self._paragraphs: list[DocxParagraph] = self.parse_paragraphs()
        self._text: str = self.parse_text()

    # GETTERS & SETTERS
    @property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, new_path: str) -> None:
        self._path = new_path

    @property
    def paragraphs(self) -> list[DocxParagraph]:
        return self._paragraphs

    @paragraphs.setter
    def paragraphs(self, new_paragraphs: list[DocxParagraph]) -> None:
        self._paragraphs = new_paragraphs

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, new_text: str) -> None:
        self._text = new_text

    # PARSING METHODS
    def parse_paragraphs(self) -> list[DocxParagraph]:
        document = ET.fromstring(ZipFile(self.path).read("word/document.xml"))
        paragraphs = document.find("w:body", self.NAMESPACE).findall("w:p", self.NAMESPACE)
        return [DocxParagraph(paragraph) for paragraph in paragraphs]

    def parse_text(self) -> str:
        return "".join([paragraph.text for paragraph in self.paragraphs])
