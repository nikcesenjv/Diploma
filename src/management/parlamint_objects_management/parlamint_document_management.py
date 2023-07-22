# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parlamint_objects_management.py

from .parlamint_objects_management import create_parlamint_note, create_parlamint_speaker, create_parlamint_utterance,  \
    create_parlamint_property_element

from src.management.json_management import parse_json
from src.management.path_management import parse_path
from src.management.parlamint_objects_management import find_attendee, is_attendee, create_parlamint_attendee
from src.management.text_management import parse_string, is_close_match_list, is_close_match_string, \
    extract_attendees_from_string

from src.objects.general_objects import File
from src.objects.parlamint_objects import ParlamintDocument, ParlamintAttendee, ParlamintHead, \
    ParlamintNote, ParlamintSpeaker, ParlamintSpeakerList

def create_parlamint_document(file: File, all_attendees_list: list[ParlamintAttendee]) -> ParlamintDocument:
    parlamint_document = ParlamintDocument(file)
    paragraph_list = [parse_string(paragraph.text) for paragraph in parlamint_document.docx_document.paragraphs
                      if len(paragraph.text) > 0]

    json_path = parse_path("path.parlamint_properties", f"parlamint_properties_{file.assembly}.json")
    property_elements = parse_json(json_path)["properties"]

    parlamint_document.elements, parlamint_document.attendees, all_attendees_list = \
        parse_parlamint_properties(property_elements, paragraph_list, all_attendees_list)

    parlamint_document.utterance_num, parlamint_document.segment_num = assign_document_statistics(parlamint_document)

    # docx_paragraphs = parlamint_document.docx_document.paragraphs
    """for attendee in parlamint_document.attendees:
        if not find_attendee(attendee.name, all_attendees):
            all_attendees.append(attendee)"""

    return parlamint_document, all_attendees_list

def parse_parlamint_properties(property_elements: dict[str, str | list], paragraph_list: list[str],
                               all_attendees_list: list[ParlamintAttendee]) \
        -> tuple[list[ParlamintHead | ParlamintNote], list[ParlamintAttendee], list[ParlamintAttendee]]:

    element_list, parlamint_attendee_list, parlamint_speakers = [], [], False
    # paragraph_list = [parse_string(paragraph.text) for paragraph in paragraphs if len(paragraph.text) > 0]

    for i, property_element in enumerate(property_elements):
        parlamint_element, next_property_elements = create_parlamint_property_element(property_element), (None, None)

        if i + 2 < len(property_elements):
            next_property_elements = property_elements[i + 1], property_elements[i + 2]
        elif i + 1 < len(property_elements):
            next_property_elements = property_elements[i + 1], None

        parlamint_element, paragraph_list = parse_parlamint_element(parlamint_element, paragraph_list,
                                                                    next_property_elements, parlamint_attendee_list)

        if "role" in property_element:
            parlamint_attendee_list = parse_parlamint_attendees(parlamint_attendee_list, all_attendees_list,
                                                                parlamint_element.paragraphs)

        if "additional elements" in property_element:
            parlamint_element = parse_additional_properties(property_element, parlamint_element,
                                                            parlamint_attendee_list, all_attendees_list)

        if isinstance(parlamint_element, list):
            element_list.extend(parlamint_element)
        elif isinstance(parlamint_element, ParlamintSpeakerList) or len(parlamint_element.paragraphs) > 0:
            element_list.append(parlamint_element)

    return element_list, parlamint_attendee_list, all_attendees_list

def parse_additional_properties(property_element, parlamint_element, parlamint_attendee_list, all_attendees_list):
    additional_properties_list = [parlamint_element]

    for additional_property in property_element["additional elements"]:
        additional_property_element = create_parlamint_property_element(additional_property)

        for i, paragraph in enumerate(additional_properties_list[-1].paragraphs):
            if is_close_match_list(paragraph, additional_property["similar words"]):
                additional_property_element.paragraphs = additional_properties_list[-1].paragraphs[i:]
                additional_properties_list[-1].paragraphs = additional_properties_list[-1].paragraphs[:i]

        if "role" in additional_property:
            parlamint_attendee_list = parse_parlamint_attendees(parlamint_attendee_list, all_attendees_list,
                                                                additional_property_element.paragraphs)

        additional_properties_list.append(additional_property_element)

    return additional_properties_list

def parse_parlamint_element(parlamint_element: ParlamintHead | ParlamintNote | ParlamintSpeakerList,
                            paragraph_list: list[str],
                            next_property_elements: tuple[dict[str, str | list] | None, dict[str, str | list]] | None,
                            parlamint_attendee_list: list[ParlamintAttendee]) \
        -> tuple[ParlamintHead | ParlamintNote | ParlamintSpeakerList, list[str]]:

    if type(parlamint_element) == ParlamintSpeakerList:
        parlamint_element.parlamint_speakers, paragraphs = parse_parlamint_speakers(paragraph_list,
                                                                                    parlamint_attendee_list,
                                                                                    next_property_elements)
        return parlamint_element, paragraph_list

    for i, paragraph in enumerate(paragraph_list):
        try:
            if is_close_match_list(paragraph, next_property_elements[1]["similar words"]) or \
                    is_close_match_list(paragraph, next_property_elements[0]["similar words"]):
                return parlamint_element, paragraph_list[i:]

            parlamint_element.add_paragraph(paragraph)

        except TypeError:
            if all(value is None for value in next_property_elements):
                parlamint_element.add_paragraph(paragraph)
            else:
                if is_close_match_list(paragraph, next_property_elements[0]["similar words"]):
                    return parlamint_element, paragraph_list[i:]

                parlamint_element.add_paragraph(paragraph)

    return parlamint_element, []

def parse_parlamint_attendees(parlamint_attendees_list: list[ParlamintAttendee],
                              all_attendees_list: list[ParlamintAttendee], paragraph_list: list[str]) \
        -> tuple[list[ParlamintAttendee]]:

    attendee_names = extract_attendees_from_string(paragraph_list)

    for attendee_name in attendee_names:
        if is_attendee(attendee_name, all_attendees_list):
            continue

        if is_close_match_string(attendee_name, "izvestilac"):
            attendee_type = "izvestilac"
        else:
            attendee_type = "regular"

        parlamint_attendees_list.append(create_parlamint_attendee(attendee_name, attendee_type))

    return parlamint_attendees_list

def parse_parlamint_speakers(paragraph_list: list[str], parlamint_attendees_list: list[ParlamintAttendee],
                             next_property_element):

    parlamint_speakers_list, current_speaker = [], None

    for i, paragraph in enumerate(paragraph_list):
        if is_close_match_list(paragraph, next_property_element[0]["similar words"]):
            parlamint_speakers_list.append(current_speaker) if current_speaker is not None else None
            return parlamint_speakers_list, paragraph_list[i:]

        if ":" in paragraph and ":" != paragraph[-1]:
            speaker, text = paragraph.split(":", 1)

            if len(speaker.split()) < 20:
                current_attendee = find_attendee(speaker, parlamint_attendees_list)

                if current_attendee is not None:
                    parlamint_speakers_list.append(current_speaker) if current_speaker is not None else None

                    parlamint_utterance = create_parlamint_utterance(current_attendee)
                    parlamint_utterance.add_paragraph(text)

                    current_speaker = create_parlamint_speaker(speaker, parlamint_utterance)
                    continue

                if isinstance(current_speaker, ParlamintNote):
                    current_speaker.add_paragraph(paragraph)
                else:
                    current_speaker.utterance.add_paragraph(paragraph)

        elif is_close_match_list(paragraph, ["čita"], threshold=90):
            parlamint_speakers_list.append(current_speaker) if current_speaker is not None else None

            current_speaker = create_parlamint_note("reading")
            current_speaker.add_paragraph(paragraph)

        else:
            if isinstance(current_speaker, ParlamintNote):
                current_speaker.add_paragraph(paragraph)
            else:
                current_speaker.utterance.add_paragraph(paragraph)

    parlamint_speakers_list.append(current_speaker) if current_speaker is not None else None
    return parlamint_speakers_list, []

"""parlamint_speakers_list, current_speaker, current_reader = [], None, None

for i, paragraph in enumerate(paragraph_list):
    if is_close_match_list(paragraph, next_property_element[0]["similar words"]):
        return parlamint_speakers_list, paragraph_list[i:]

    if is_close_match_list(paragraph, ["čita", "pročita"], 90):
        parlamint_speakers_list, current_speaker, current_reader = add_to_speakers_list(parlamint_speakers_list,
                                                                                        current_speaker,
                                                                                        current_reader)
        current_reader = create_parlamint_note("reading")
        current_reader.add_paragraph(paragraph.replace(":", "", 1))

    elif ":" in paragraph and ":" != paragraph[-1]:
        speaker, text = paragraph.split(":", 1)

        attendee = None
        if len(speaker.split()) < 20:
            attendee = find_attendee(speaker, parlamint_attendees_list)

        if attendee is not None:
            parlamint_speakers_list, current_speaker, current_reader = add_to_speakers_list(parlamint_speakers_list,
                                                                                            current_speaker,
                                                                                            current_reader)
            parlamint_utterance = create_parlamint_utterance(attendee)
            parlamint_utterance.add_paragraph(text)

            current_speaker = create_parlamint_speaker(speaker, parlamint_utterance)
            continue

        current_speaker, current_reader = add_to_speaker_reader(current_speaker, current_reader, paragraph)

    else:
        if current_speaker is not None:
            current_speaker.utterance.add_paragraph(paragraph)
        else:
            current_reader.add_paragraph(paragraph)"""

"""speakers_list, current_speaker, current_reader = [], None, None

for i, paragraph in enumerate([paragraph for paragraph in paragraph_list[:-1] if paragraph != ""]):
    paragraph = parse_string(paragraph)

    x = is_close_match_string(paragraph, "čita", 90)
    if x is not None:
        speakers_list = add_to_speakers_list(speakers_list, current_speaker, current_reader)
        current_speaker, current_reader = None, None

        current_reader = create_parlamint_note("reading", paragraph.replace(":", "", 1))

    elif ":" in paragraph and ":" != paragraph[-1]:
        speaker, text = paragraph.split(":", 1)

        if len(speaker.split()) < 20:
            attendee = find_attendee(speaker, parlamint_attendees)
        else:
            attendee = None

        if attendee is not None:
            speakers_list = add_to_speakers_list(speakers_list, current_speaker, current_reader)
            current_speaker, current_reader = None, None

            parlamint_utterance = create_parlamint_utterance(attendee)
            parlamint_utterance.add_paragraph(text)

            current_speaker = create_parlamint_speaker(speaker, parlamint_utterance)
            continue

        current_speaker, current_reader = add_to_speaker_reader(current_speaker, current_reader, paragraph)

    else:
        if current_speaker is not None:
            current_speaker.utterance.add_paragraph(paragraph)
        else:
            current_reader.add_paragraph(paragraph)

    speakers_list = add_to_speakers_list(speakers_list, current_speaker, current_reader)
    return speakers_list, [paragraphs[-1]]"""

"""parlamint_speakers_list, _, _ = add_to_speakers_list(parlamint_speakers_list, current_speaker, current_reader)
return parlamint_speakers_list, []"""

def assign_document_statistics(parlamint_document: ParlamintDocument) -> tuple[int, int]:
    utterance_num, segment_num = 0, 1

    for element_list in parlamint_document.elements:
        if not isinstance(element_list, ParlamintSpeakerList):
            continue

        for element in element_list.parlamint_speakers:
            if not isinstance(element, ParlamintSpeaker):
                continue

            element.utterance.document_id = parlamint_document.document_id
            element.utterance.utterance_num = utterance_num
            utterance_num += 1

            element.utterance.segment_start_num = segment_num
            segment_num += len(element.utterance.paragraphs)

    return utterance_num - 1, segment_num


