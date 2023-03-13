# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_document.py

import xml.etree.ElementTree as ET

from src.parsing import DocxDocument
from src.parsing import File

class ParlamintDocument:
    def __init__(self, file, docx_document, original_text=True):
        self._file: File = file
        self._docx_document: DocxDocument = docx_document

        self._original_text: bool = original_text

        # self._xml_path = self._file.xml_path

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

    def write_xml(self) -> None:
        tei = self.initialize_xml_file()
        self.initialize_tei_header(tei)

        self.save_xml_file(tei)

        """tei_element = ET.Element("TEI", xmlns="http://www.tei-c.org/ns/1.0")
        tei_element.set("xml:id", "test")"""

        """tei_element = self.write_tei_xml()
        tei = self.write_tei_header_xml(tei_element)
        file_desc = self.write_file_desc_xml(tei)
        _ = self.write_title_stmt_xml(file_desc)

        tree = ET.ElementTree(tei_element)
        ET.indent(tree)
        tree.write("/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/text2.xml", encoding="UTF-8",
                   xml_declaration=True)"""

        """xml_doc = ET.Element("root")

        tree = ET.ElementTree(xml_doc)
        ET.indent(tree)
        tree.write("/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/text.xml", encoding="UTF-8", xml_declaration=True)"""

    def initialize_xml_file(self) -> ET:
        tei = ET.Element("TEI", xmlns="http://www.tei-c.org/ns/1.0")
        # tei.set("xml:id", self._file.name)
        tei.set("xml:id", "test123")
        tei.set("xml:lang", "sl")
        tei.set("ana", "#parla.sitting #reference")
        return tei

    def initialize_tei_header(self, parent_element: ET) -> ET:
        tei_header = ET.SubElement(parent_element, "teiHeader")

        self.initialize_file_desc(tei_header)
        ET.SubElement(tei_header, "encodingDesc")

    def initialize_file_desc(self, parent_element):
        file_desc = ET.SubElement(parent_element, "fileDesc")
        self.initialize_title_stmt(file_desc)

    def initialize_title_stmt(self, parent_element: ET) -> ET:
        title_stmt = ET.SubElement(parent_element, "titleStmt")

        title_main_sl = ET.SubElement(title_stmt, "title", type="main")
        title_main_sl.set("xml:lang", "sl")
        title_main_sl.text = "STENOGRAFSKE BELEŽKE"

        title_main_en = ET.SubElement(title_stmt, "title", type="main")
        title_main_en.set("xml:lang", "en")
        title_main_en.text = "STENOGRAPHY"

        title_sub_sl = ET.SubElement(title_stmt, "title", type="sub")
        title_sub_sl.set("xml:lang", "en")
        title_sub_sl.text = "sub slo"

        title_sub_en = ET.SubElement(title_stmt, "title", type="sub")
        title_sub_en.set("xml:lang", "en")
        title_sub_en.text = "sub eng"

        meeting_type = ET.SubElement(title_stmt, "meeting", n="2", corresp="#DZ")
        meeting_type.text = "Redna"

        meeting_num = ET.SubElement(title_stmt, "meeting", n="7", corresp="#DZ")
        meeting_num.text = "7. mandat"

        self.initialize_resp_stmt(title_stmt)
        self.initialize_funder(title_stmt)

    def initialize_resp_stmt(self, parent_element):
        resp_stmt = ET.SubElement(parent_element, "respStmt")

        ET.SubElement(resp_stmt, "persName").text = "Nik Česenj Vodovnik"

        resp_sl = ET.SubElement(resp_stmt, "resp")
        resp_sl.set("xml:lang", "sl")
        resp_sl.text = "Kodiranje TEI"

        resp_en = ET.SubElement(resp_stmt, "resp")
        resp_en.set("xml:lang", "en")
        resp_en.text = "TEI corpus encoding"

    def initialize_funder(self, parent_element):
        funder = ET.SubElement(parent_element, "funder")

        org_name_sl = ET.SubElement(funder, "orgName")
        org_name_sl.set("xml:lang", "sl")
        org_name_sl.text = "Raziskovalna infrastruktura CLARIN"

        org_name_en = ET.SubElement(funder, "orgName")
        org_name_en.set("xml:lang", "en")
        org_name_en.text = "The CLARIN research infrastructure"

    def initialize_encoding_desc(self, parent_element):
        return ET.SubElement(parent_element, "encodingDesc")

    def initialize_text(self, parent_element: ET) -> ET:
        ET.SubElement(parent_element, "teiHeader")

    def save_xml_file(self, xml_document: ET):
        tree = ET.ElementTree(xml_document)
        ET.indent(tree, space="    ")
        tree.write("/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/text2.xml", encoding="UTF-8", xml_declaration=True)

    """@staticmethod
    def write_tei_xml() -> ET:
        tei_element = ET.Element("TEI", xmlns="http://www.tei-c.org/ns/1.0")
        tei_element.set("xml:id", "test")
        tei_element.set("xml:lang", "sl")
        tei_element.set("ana", "#parla.sitting #reference")
        return tei_element

    @staticmethod
    def write_tei_header_xml(parent_element: ET) -> ET:
        return ET.SubElement(parent_element, "teiHeader")

    @staticmethod
    def write_file_desc_xml(parent_element: ET) -> ET:
        return ET.SubElement(parent_element, "fileDesc")

    def write_title_stmt_xml(self, parent_element: ET) -> ET:
        title_stmt = ET.SubElement(parent_element, "titleStmt")

        title_main_sl = ET.SubElement(title_stmt, "title", type="main")
        title_main_sl.set("xml:lang", "sl")
        title_main_sl.text = "Raziskovalna naloga"

        title_main_en = ET.SubElement(title_stmt, "title", type="main")
        title_main_en.set("xml:lang", "en")
        title_main_en.text = "Research"

        title_sub_sl = ET.SubElement(title_stmt, "title", type="sub")
        title_sub_sl.set("xml:lang", "sl")
        title_sub_sl.text = "TEST ENA"

        title_sub_en = ET.SubElement(title_stmt, "title", type="sub")
        title_sub_en.set("xml:lang", "en")
        title_sub_en.text = "TEST ONE"

        meeting = ET.SubElement(title_stmt, "meeting", n=f"{self._file.index}")

        return title_stmt"""


document = ParlamintDocument(None, None)
