import xml.etree.ElementTree as ET

def initialize_file_desc(parent_element):
    file_desc = ET.SubElement(parent_element, "fileDesc")
    initialize_title_stmt(file_desc)


def initialize_title_stmt(parent_element: ET) -> ET:
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


def initialize_text(parent_element: ET) -> ET:
    ET.SubElement(parent_element, "teiHeader")
