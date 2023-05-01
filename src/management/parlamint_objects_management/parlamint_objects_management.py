# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_objects_management.py

from src.logging import log

from src.management.json_management import parse_json
from src.management.text_management import close_match

from src.objects.docx_objects import DocxDocument, DocxParagraph
from src.objects.parlamint_objects import ParlamintDiv, ParlamintDocument, ParlamintHead, ParlamintNote, \
    ParlamintSpeaker

def create_parlamint_object(docx_document: DocxDocument) -> list[ParlamintDiv | ParlamintHead | ParlamintNote]:
    parlamint_document = ParlamintDocument(docx_document)
    paragraphs = parlamint_document.docx_document.paragraphs

    parlamint_properties = parse_json("/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/lib/resources/json_resources/parlamint_properties.json")
    parlamint_document.elements = parse_parlamint_properties(parlamint_properties["properties"], paragraphs)

    # parlamint_document.docx_document.print_xml()

    return parlamint_document

def parse_parlamint_properties(parlamint_properties: dict[str, str | list], paragraphs: list[DocxParagraph]):
    element_list = []

    for element in parlamint_properties:
        try:
            func = globals()["create_" + element["tag"] + "_element"]
            parlamint_element, paragraphs = func(element, paragraphs)
            element_list.append(parlamint_element)
        except KeyError:
            log("WARNING", "find_objects.key.error", element["tag"])

    return element_list

def create_div_element(properties_element: dict[str, str | list], paragraphs: list[DocxParagraph]) -> ParlamintDiv:
    parlamint_div = ParlamintDiv(properties_element["type"])

    for element in properties_element["elements"]:
        try:
            func = globals()["create_" + element["tag"] + "_element"]
            parlamint_element, paragraphs = func(element, paragraphs)
            parlamint_div.add_element(parlamint_element)
        except KeyError:
            log("WARNING", "find_objects.key.error", element["tag"])

    return parlamint_div, paragraphs

def create_head_element(properties_element: dict[str, str], paragraphs: list[DocxParagraph]) -> ParlamintHead:
    parlamint_head = ParlamintHead(properties_element["type"])

    for i, paragraph in enumerate(paragraphs):
        if close_match(properties_element["similar words"], paragraph.text):
            parlamint_head.add_paragraph(paragraph)
        else:
            return parlamint_head, paragraphs[i:]
        """if any(similar_word in paragraph.text for similar_word in properties_element["similar words"]):
            parlamint_head.add_paragraph(paragraph)
        else:
            return parlamint_head, paragraphs[i:]"""

def create_note_element(properties_element: dict[str, str], paragraphs: list[DocxParagraph]) -> ParlamintNote:
    parlamint_note = ParlamintNote(properties_element["type"])
    return parlamint_note, paragraphs

def create_speaker_element(properties_element: dict[str, str], paragraphs: list[DocxParagraph]) -> ParlamintSpeaker:
    speaker_paragraphs = []
    first_bold = False

    # parlamint_note = ParlamintNote()
    # parlamint_utterance = ParlamintUtterance()
    # parlamint_speaker = ParlamintSpeaker(parlamint_note, parlamint_utterance)
    return None, paragraphs

def create_utterance_element():
    ...
