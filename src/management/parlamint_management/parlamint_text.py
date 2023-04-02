# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_text.py

import xml.etree.ElementTree as ET

from src.objects.parlamint_objects import ParlamintAttendee

def initialize_text(parent_element: ET) -> ET:
    text = ET.SubElement(parent_element, "text")
    text.set("ana", "#reference")

    initalize_body(text)

    return text

def initalize_body(parent_element: ET) -> None:
    body = ET.SubElement(parent_element, "body")

    initialize_div(body)

def initialize_div(parent_element: ET) -> None:
    ET.SubElement(parent_element, "div", type="debateSection")

def initialize_head(parent_element: ET, head_text: str, head_type: str = None) -> None:
    head = ET.SubElement(parent_element, "head")

    if head_type is not None:
        head.set("type", head_type)

    head.text = head_text

# FLEXIBLE
def initialize_flexible_element(parent_element: ET, xml_object):
    ...
