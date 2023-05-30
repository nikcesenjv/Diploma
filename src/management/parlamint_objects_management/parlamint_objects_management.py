# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_objects_management.py

from docx.text.paragraph import Paragraph

from .parlamint_attendee_management import is_attendee

from src.logging import log

from src.management.json_management import parse_json
from src.management.text_management import *
from src.management.parlamint_objects_management import find_attendee
from src.management.path_management import parse_path

from src.objects.general_objects import File
from src.objects.parlamint_objects import ParlamintDocument, ParlamintAttendee, ParlamintHead, \
    ParlamintNote, ParlamintDiv, ParlamintSpeaker, ParlamintUtterance

def create_parlamint_document(file: File, attendees: list[ParlamintAttendee]) -> ParlamintDocument:
    parlamint_document = ParlamintDocument(file)
    docx_paragraphs = parlamint_document.docx_document.paragraphs

    json_path = parse_path("path.parlamint_properties", f"parlamint_properties_{file.assembly}.json")
    properties = parse_json(json_path)["properties"]

    parlamint_document.elements, parlamint_document.attendees, all_attendees = \
        parse_parlamint_properties(properties, docx_paragraphs, attendees)

    parlamint_document, _, _ = assign_document_statistics(parlamint_document)

    for attendee in parlamint_document.attendees:
        if not find_attendee(attendee.name, all_attendees):
            all_attendees.append(attendee)

    return parlamint_document, all_attendees

def assign_document_statistics(parlamint_document: ParlamintDocument) -> tuple[ParlamintDocument, int, int]:
    utterance_num, segment_num = 1, 1

    for element in parlamint_document.elements:
        if type(element) == ParlamintSpeaker:
            element.utterance.document_id = parlamint_document.document_id
            element.utterance.utterance_num = utterance_num
            utterance_num += 1

            element.utterance.segment_start_num = segment_num
            segment_num += len(element.utterance.paragraphs)

    return parlamint_document, utterance_num - 1, segment_num


def parse_parlamint_properties(properties: dict[str, str | list], paragraphs: list[Paragraph],
                               attendees: list[ParlamintAttendee]) \
        -> tuple[list[ParlamintDiv, ParlamintHead | ParlamintNote], list[ParlamintAttendee], list[ParlamintAttendee]]:

    element_list, parlamint_attendees, parlamint_speakers, parlamint_element = [], [], [], None

    for i, property_element in enumerate(properties):
        match property_element["tag"]:
            case "head":
                parlamint_element = ParlamintHead(property_element["type"])
            case "note":
                parlamint_element = ParlamintNote(property_element["type"])
            case "speakers":
                parlamint_speakers, paragraphs = parse_parlamint_speakers(parlamint_attendees, paragraphs)

        try:
            property_elements = properties[i + 1], properties[i + 2]
            parlamint_element.paragraphs, paragraphs = parse_parlamint_element(property_elements, paragraphs)

            if "role" in property_element:
                parlamint_attendees.extend(parse_parlamint_attendees(property_element, attendees,
                                                                     parlamint_element.paragraphs))

            if len(parlamint_element.paragraphs) > 0:
                element_list.append(parlamint_element)

        except IndexError:
            if len(parlamint_speakers) > 0:
                element_list.extend(parlamint_speakers)
                parlamint_speakers = []
            else:
                parlamint_element.paragraphs, paragraphs = parse_parlamint_element(property_element, paragraphs)

    return element_list, parlamint_attendees, attendees

def parse_parlamint_element(properties: tuple[dict[str, str | list], dict[str, str | list]],
                            paragraphs: list[Paragraph]) -> list[Paragraph]:

    element_paragraphs = []

    for i, paragraph in enumerate([paragraph for paragraph in paragraphs if paragraph.text != ""]):
        try:
            """if is_close_match_list(paragraph.text, properties[1]["similar words"]):
                return element_paragraphs, paragraphs[i:]

            elif not is_close_match_list(paragraph.text, properties[0]["similar words"]):
                element_paragraphs.append(paragraph.text)"""
            if closest_substring(paragraph.text, " ".join(properties[1]["similar words"])) is not None:
                return element_paragraphs, paragraphs[i:]
            elif closest_substring(paragraph.text, " ".join(properties[0]["similar words"])) is None:
                element_paragraphs.append(paragraph.text)

            else:
                return element_paragraphs, paragraphs[i:]

        except KeyError:
            """if is_close_match_list(paragraph.text, properties["similar words"]):
                return element_paragraphs.append(paragraph.text), []"""
            if closest_substring(paragraph.text, " ".join(properties[1]["similar words"])) is None:
                return element_paragraphs.append(paragraph.text), []

def parse_parlamint_attendees(property_element: dict[str, str | list], attendees: list[ParlamintAttendee],
                              paragraphs: list[Paragraph]) -> list[ParlamintAttendee]:

    parlamint_document_attendees = []
    attendee_names = remove_close_matches(" ".join(paragraphs), property_element["similar words"])

    for attendee_name in attendee_names.replace("\n", " ").split(", "):
        if not is_attendee(attendee_name, attendees):
            if closest_substring(attendee_name, "izvestilac") is not None:
                attendee_name = remove_close_matches(attendee_name, ["izvestilac"])
                parlamint_document_attendees.append(create_parlamint_attendee(attendee_name, "reporter"))

            else:
                parlamint_document_attendees.append(create_parlamint_attendee(attendee_name, property_element["role"]))

    return parlamint_document_attendees

def create_parlamint_attendee(name: str, attendee_type: str):
    return ParlamintAttendee(name, attendee_type)

def create_parlamint_speaker(speaker: str, parlamint_utterance: ParlamintUtterance):
    parlamint_note = create_parlamint_note("speaker", speaker)
    return ParlamintSpeaker(parlamint_note, parlamint_utterance)

def create_parlamint_note(note_type: str, string: str):
    parlamint_note = ParlamintNote(note_type)
    parlamint_note.add_paragraph(string)
    return parlamint_note

def create_parlamint_utterance(attendee: ParlamintAttendee):
    parlamint_utterance = ParlamintUtterance(attendee)
    return parlamint_utterance


def parse_parlamint_speakers(attendees: list[ParlamintAttendee], paragraphs: list[Paragraph])\
        -> list[ParlamintSpeaker]:

    speakers_list, current_speaker = [], None

    for paragraph in [paragraph for paragraph in paragraphs if paragraph.text != ""]:
        paragraph.text = paragraph.text.replace("\n", "")

        if closest_substring(paragraph.text, "čita") is not None:
            if current_speaker is not None:
                speakers_list.append(current_speaker)
                current_speaker = None

            speakers_list.append(create_parlamint_note("reading", paragraph.text.replace(":", "", 1)))

        elif ":" in paragraph.text:
            speaker, text = paragraph.text.split(":", 1)
            attendee = find_attendee(speaker, attendees)

            if attendee is not None:
                if current_speaker is not None:
                    speakers_list.append(current_speaker)

                parlamint_utterance = create_parlamint_utterance(attendee)
                parlamint_utterance.add_paragraph(text)
                current_speaker = create_parlamint_speaker(speaker, parlamint_utterance)
            else:
                current_speaker.utterance.add_paragraph(paragraph.text)

        elif str(paragraph.alignment) == "CENTER (1)":
            if current_speaker is not None:
                speakers_list.append(current_speaker)
                current_speaker = None
            speakers_list.append(create_parlamint_note("test", paragraph.text))

        else:
            current_speaker.utterance.add_paragraph(paragraph.text)

    if current_speaker is not None:
        speakers_list.append(current_speaker)

    return speakers_list, [paragraphs[-1]]
