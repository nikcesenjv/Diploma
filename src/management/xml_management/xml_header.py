# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka xml_header.py

import xml.etree.ElementTree as ET

from .xml_header_management import *

from src.objects.parlamint_objects import ParlamintDocument

def initialize_tei_header(parent_element: ET, parlamint_document: ParlamintDocument):
    tei_header = ET.SubElement(parent_element, "teiHeader")
    initialize_file_desc(tei_header, parlamint_document)

    initialize_encoding_desc(tei_header)

def initialize_file_desc(parent_element: ET, parlamint_document: ParlamintDocument):
    file_desc = ET.SubElement(parent_element, "fileDesc")
    initialize_title_stmt(file_desc, parlamint_document.document)

def initialize_title_stmt(parent_element: ET, file: Document) -> ET:
    title_stmt = ET.SubElement(parent_element, "titleStmt")

    title_main_sl = ET.SubElement(title_stmt, "title", type="main")
    title_main_sl.set("xml:lang", "sl")
    title_main_sl.text = parlamint_main_title_sl(file)

    title_main_en = ET.SubElement(title_stmt, "title", type="main")
    title_main_en.set("xml:lang", "en")
    title_main_en.text = parlamint_main_title_en(file)

    title_sub_sl = ET.SubElement(title_stmt, "title", type="sub")
    title_sub_sl.set("xml:lang", "sl")
    title_sub_sl.text = parlamint_sub_title_sl(file)

    title_sub_en = ET.SubElement(title_stmt, "title", type="sub")
    title_sub_en.set("xml:lang", "en")
    title_sub_en.text = parlaming_sub_title_en(file)

    meeting_type = ET.SubElement(title_stmt, "meeting", n=str(file.num_arab), corresp=f"#{file.assembly}")
    meeting_type_text, ana_reference_type = parlamint_meeting_type(file)
    meeting_type.set("ana", ana_reference_type)
    meeting_type.text = meeting_type_text

    meeting_num = ET.SubElement(title_stmt, "meeting", n=str(file.index), corresp=f"#{file.assembly}")
    meeting_num_text, ana_reference_num = parlamint_meeting_num(file)
    meeting_num.set("ana", ana_reference_num)
    meeting_num.text = meeting_num_text

    initialize_resp_stmt(title_stmt)
    initialize_funder(title_stmt)

def initialize_resp_stmt(parent_element):
    resp_stmt = ET.SubElement(parent_element, "respStmt")

    ET.SubElement(resp_stmt, "persName").text = "Nik Česenj Vodovnik"

    resp_sl = ET.SubElement(resp_stmt, "resp")
    resp_sl.set("xml:lang", "sl")
    resp_sl.text = "Kodiranje TEI"

    resp_en = ET.SubElement(resp_stmt, "resp")
    resp_en.set("xml:lang", "en")
    resp_en.text = "TEI corpus encoding"

def initialize_funder(parent_element):
    funder = ET.SubElement(parent_element, "funder")

    org_name_sl = ET.SubElement(funder, "orgName")
    org_name_sl.set("xml:lang", "sl")
    org_name_sl.text = "Raziskovalna infrastruktura CLARIN"

    org_name_en = ET.SubElement(funder, "orgName")
    org_name_en.set("xml:lang", "en")
    org_name_en.text = "The CLARIN research infrastructure"

def initialize_encoding_desc(parent_element):
    return ET.SubElement(parent_element, "encodingDesc")
