# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_document.py

import xml.etree.ElementTree as ET

import bs4

from zipfile import ZipFile

from .docx_paragraph import DocxParagraph
from .element_parser import ElementParser

from src.management.path_management import parse_path

from src.objects.general_objects import File

class DocxDocument(ElementParser):
    def __init__(self, file: File):
        # self._path: str = path
        self._file: File = file

        self._paragraphs: list[DocxParagraph] = self.parse_paragraphs()
        self._text: str = self.parse_text()

    # GETTERS & SETTERS
    @property
    def file(self) -> File:
        return self._file

    @file.setter
    def file(self, new_file: File) -> None:
        self._file = new_file

    """@property
    def path(self) -> str:
        return self._path

    @path.setter
    def path(self, new_path: str) -> None:
        self._path = new_path"""

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
        document = ZipFile(parse_path("full_path.documents", self.file.word_path))
        xml_document_string = ET.fromstring(document.read("word/document.xml"))
        paragraphs = xml_document_string.find("w:body", self.NAMESPACE).findall("w:p", self.NAMESPACE)
        return [DocxParagraph(paragraph) for paragraph in paragraphs]

    def parse_text(self) -> str:
        return "".join([paragraph.text for paragraph in self.paragraphs])

    """def print_xml(self) -> None:
        document = ET.fromstring(ZipFile(self.path).read("word/document.xml"))

        x = ET.tostring(document)
        t = bs4.BeautifulSoup(x).prettify()

        print(t)"""


# x = DocxDocument("/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/lib/documents/word/19_1932_SKJ/18-40_redni/9_XXVI_SKJ_redni_15.4.1932.docx")
# x.print_xml()

def test(document: DocxDocument) -> None:
    """_ = merge_paragraphs(document.paragraphs[0], document.paragraphs[1])
    del document.paragraphs[1]"""

    """for i, element in enumerate(document.ELEMENT_TYPES):
        print(i, document.find_element(element), element)
        print(document.paragraphs[i].text)
        print()"""

    for p in document.paragraphs:
        print(p.text)

def merge_paragraphs(*paragraphs: list[DocxParagraph]):
    for paragraph in paragraphs[1:]:
        paragraphs[0].text += "\n"
        paragraphs[0].text += paragraph.text

    return paragraphs[0]

# test(x)
