"""def create_parlamint_xml_document(parlamint_document: ParlamintDocument, target_path: str) -> None:
    xml_document = initialize_xml_file(parlamint_document.document_id)

    initialize_tei_header(xml_document, parlamint_document)
    text_element = initialize_text(xml_document)

    for xml_object in parlamint_document.objects:
        xml_object.to_element(text_element)

    parlamint_document.xml_element = xml_document
    save_xml_file(xml_document, target_path)

def initialize_xml_file(document_name: str) -> ET:
    tei = ET.Element("TEI", xmlns="http://www.tei-c.org/ns/1.0")
    tei.set("xml:id", document_name)
    tei.set("xml:lang", "sr")
    tei.set("ana", "#parla.sitting #reference")
    return tei

def save_xml_file(xml_document: ET, target_path: str) -> None:
    tree = ET.ElementTree(xml_document)
    ET.indent(tree, space="    ")
    tree.write(target_path, encoding="UTF-8", xml_declaration=True)"""

# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_management.py

from src.management.json_management import parse_json
from src.management.path_management import parse_path

from src.objects.docx_objects import DocxDocument
from src.objects.parlamint_objects import ParlamintDocument

def create_parlamint_xml_document(parlamint_document: ParlamintDocument, target_path: str) -> None:
    xml_document = initialize_xml_file(parlamint_document.document_id)

    initialize_tei_header(xml_document, parlamint_document)
    text_element = initialize_text(xml_document)

    for xml_object in parlamint_document.objects:
        xml_object.to_element(text_element)

    parlamint_document.xml_element = xml_document
    save_xml_file(xml_document, target_path)

def initialize_xml_file(document_name: str) -> ET:
    tei = ET.Element("TEI", xmlns="http://www.tei-c.org/ns/1.0")
    tei.set("xml:id", document_name)
    tei.set("xml:lang", "sr")
    tei.set("ana", "#parla.sitting #reference")
    return tei

def save_xml_file(xml_document: ET, target_path: str) -> None:
    tree = ET.ElementTree(xml_document)
    ET.indent(tree, space="    ")
    tree.write(target_path, encoding="UTF-8", xml_declaration=True)
