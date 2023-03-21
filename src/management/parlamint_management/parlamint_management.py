import xml.etree.ElementTree as ET

from src.objects.parlamint_objects import ParlamintDocument

from .create_parlamint_header import initialize_file_desc

def create_parlamint_document():
    ...

def initialize_xml_file():
    tei = ET.Element("TEI", xmlns="http://www.tei-c.org/ns/1.0")
    tei.set("xml:id", "test123")
    tei.set("xml:lang", "sl")
    tei.set("ana", "#parla.sitting #reference")
    return tei

def initialize_tei_header(parent_element):
    tei_header = ET.SubElement(parent_element, "teiHeader")

    initialize_file_desc(tei_header)
    ET.SubElement(tei_header, "encodingDesc")

def save_xml_file(xml_document: ET):
    tree = ET.ElementTree(xml_document)
    ET.indent(tree, space="    ")
    tree.write("/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/text2.xml", encoding="UTF-8", xml_declaration=True)