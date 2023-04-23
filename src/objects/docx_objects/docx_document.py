# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_document.py

import xml.etree.ElementTree as ET

from zipfile import ZipFile

from .docx_element import DocxElement
from .docx_paragraph import DocxParagraph
from .element_parser import ElementParser

from src.objects.general_objects import File

class DocxDocument(ElementParser):

    root_path = "/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/lib/documents/"

    def __init__(self, file: File):
        self._file: File = file

        self._paragraphs: list[DocxParagraph] = self.parse_paragraphs()
        self._text: str = self.parse_text()

        self._elements: list[DocxElement] = []

    # GETTERS & SETTERS
    @property
    def file(self) -> File:
        return self._file

    @file.setter
    def file(self, new_file: File) -> None:
        self._file = new_file

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

    @property
    def elements(self) -> list[DocxElement]:
        return self._elements

    @elements.setter
    def elements(self, new_elements: list[DocxElement]) -> None:
        self._elements = new_elements

    # PARSING METHODS
    def parse_paragraphs(self) -> list[DocxParagraph]:
        document = ET.fromstring(ZipFile(self.root_path + self.file.word_path).read("word/document.xml"))
        paragraphs = document.find("w:body", self.NAMESPACE).findall("w:p", self.NAMESPACE)
        return [DocxParagraph(paragraph) for paragraph in paragraphs]

    def parse_paragraphs_real(self) -> dict[str, list[DocxParagraph]]:
        parsed_document = {}
        _ = ET.fromstring(ZipFile(self.root_path + self.file.word_path).read("word/document.xml"))

        return parsed_document

    def parse_text(self) -> str:
        return "".join([paragraph.text for paragraph in self.paragraphs])

    def print_xml(self) -> ET:
        document = ET.fromstring(ZipFile(self.root_path + self.file.word_path).read("word/document.xml"))
        print(document)
