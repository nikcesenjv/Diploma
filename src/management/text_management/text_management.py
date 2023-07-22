# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka text_management.py

import re

from cyrtranslit import to_latin
from fuzzywuzzy import fuzz, process

def cyrillic_to_latin_text(text: str) -> str:
    return to_latin(text, "sr")

def get_text(path):
    with open(path, "r") as file:
        return to_latin(file.read(), "sr")

def only_normal_characters(string: str) -> str:
    return cyrillic_to_latin_text(string.lower())

def parse_string(string: str) -> str:
    return cyrillic_to_latin_text(string.replace("-\n", "").replace("\n", " ").replace("-", ""))
    # return string.replace("-\n", "").replace("\n", " ").replace("-", "")

"""def is_close_match(string: str, string_list: str | list[str], threshold: int = 75, word_length: int = 3) -> bool:
    string_split = split_string_by_words(cyrillic_to_latin_text(string))

    if type(string_list) == str:
        return fuzz.ratio(string, string_list) >= threshold
    else:
        for word in [word for word in string_split if len(word) > word_length]:
            best_match, similarity = process.extractOne(word, string_list)
            if len(best_match) > word_length and similarity >= threshold:
                return True

        return False"""

def is_close_match_list(string: str, string_list: list[str], threshold: int = 80, word_min_length: int = 3) -> bool:
    for word in [word for word in split_string_by_words(only_normal_characters(string)) if len(word) > word_min_length]:
        best_match, similarity = process.extractOne(word, string_list)
        if len(best_match) > word_min_length and similarity >= threshold:
            return True
    return False

def is_close_match_string(string_one: str, string_two: str, threshold: int = 75) -> bool:
    x = fuzz.ratio(only_normal_characters(string_one), only_normal_characters(string_two))
    return x >= threshold

def is_close_match_attendee(string_one: str, string_two: str, threshold: int = 75) -> bool:
    string_list, string_two = split_string_by_words(only_normal_characters(string_one)), \
        only_normal_characters(string_two)

    for i in range(len(string_list)):
        for j in range(len(string_list) - i):
            x = " ".join(string_list[j:i + j + 1])
            if fuzz.ratio(x, string_two) >= threshold:
                """print(f"first:  {x}")
                print(f"second: {string_two}")
                print()"""
                return True

    """res = closest_longest_substring(string_one, string_two)
    if res is not None:
        return True"""

    """string_list_one, string_list_two = split_string_by_words(only_normal_characters(string_one)), \
        split_string_by_words(only_normal_characters(string_two))

    for i in range(len(string_list_two)):
        for j in range(len(string_list_two) - i):
            x = " ".join(string_list_one[j:i + j + 1])
            if fuzz.ratio(x, string_two) >= threshold:
                print(x, string_two)
                print()
                return True"""

    return False

def close_matches_to_remove(string_list_one: list[str], string_list_two: list[str], threshold: int = 75) -> list[str]:
    close_matches = []

    for word in string_list_one:
        matches = process.extractBests(word, string_list_two, score_cutoff=threshold, limit=1)
        if matches:
            close_matches.append(word)

    return close_matches

def remove_close_matches(string: str, string_list: list[str]) -> str:
    string = cyrillic_to_latin_text(string)
    close_matches = close_matches_to_remove(split_string_by_words(string), string_list)

    for word in close_matches:
        string = string.replace(f"{word} ", "").replace(f"{word}\n", "")

    return string

def closest_substring(first_string: str, second_string: str, treshold: int = 80) -> str:
    longest_match, max_similarity_ratio = "", 0
    first_string, second_string = only_normal_characters(first_string), \
        only_normal_characters(second_string)

    for first_word in re.findall(r"\w+", first_string):
        for second_word in re.findall(r"\w+", second_string):
            similarity_ratio = fuzz.ratio(first_word, second_word)

            if similarity_ratio > max_similarity_ratio or \
                    (similarity_ratio == max_similarity_ratio and len(first_word) > len(longest_match)):

                longest_match = first_word
                max_similarity_ratio = similarity_ratio

    if max_similarity_ratio > treshold:
        return longest_match

    return None

def has_similar_string(substring, longer_string, threshold=75):
    for word in longer_string.split():
        similarity_score = fuzz.ratio(substring, word)
        if similarity_score >= threshold:
            return True
    return False

def extract_attendees_from_string(paragraphs: list[str]) -> list[str]:
    """for segment in string.strip(".").split(", "):
        if ":" in segment:
            segment = segment.split(": ")[1]

        for word in reversed(split_string_by_words(segment)):
            word_latin = cyrillic_to_latin_text(word)

            if closest_substring(word_latin, "izvestilac") is not None \
                    or closest_substring(word_latin, "dr") is not None:
                attendee_names_list.append(f"{word} {join_string_list(temporary_list, ' ', reverse=True)}")
                temporary_list = []
                break

            elif word[0].isupper():
                temporary_list.append(word)

            else:
                if len(temporary_list) > 1:
                    attendee_names_list.append(join_string_list(temporary_list, " ", reverse=True))
                    temporary_list = []
                break

    if len(temporary_list) > 0:
        attendee_names_list.append(join_string_list(temporary_list, " ", reverse=True))
    return attendee_names_list"""

    attendee_names_list, temporary_list = [], []
    paragraphs = [paragraph.replace(".", "").replace(";", ",") for paragraph in paragraphs if len(paragraph.split(" ")) > 1]

    for paragraph in paragraphs:
        paragraph = " ".join([word for word in paragraph.split(" ") if ":" not in word])

        for segment in paragraph.split(", "):
            segment_latin = cyrillic_to_latin_text(segment)

            for word in reversed(segment_latin.split(" ")):
                if closest_substring(word, "izvestilac") is not None \
                        or closest_substring(word, "dr") is not None:
                    attendee_names_list.append(f"{word} {join_string_list(temporary_list, ' ', reverse=True)}")
                    temporary_list = []
                    break

                elif word[0].isupper():
                    temporary_list.append(word)

                else:
                    if len(temporary_list) > 0:
                        attendee_names_list.append(join_string_list(temporary_list, " ", reverse=True))
                        temporary_list = []
                    break

            if len(temporary_list) > 0:
                attendee_names_list.append(join_string_list(temporary_list, " ", reverse=True))
                temporary_list = []

    if len(temporary_list) > 0:
        attendee_names_list.append(join_string_list(temporary_list, " ", reverse=True))
    return attendee_names_list

def join_string_list(string_list: list[str], delimiter: str, reverse: bool = False):
    if not reverse:
        return delimiter.join(string_list)

    return delimiter.join(reversed(string_list))

def closest_longest_substring(str1, str2):
    longest_substring = ""

    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring = str1[i:j]

            if substring in str2:
                substring_score = fuzz.ratio(substring, str2)

                if len(substring) > len(longest_substring):
                    longest_substring = substring
                elif len(substring) == len(longest_substring) and substring_score > fuzz.ratio(longest_substring, str2):
                    longest_substring = substring

    return longest_substring

def only_letters(string: str) -> bool:
    return all(letter.isalpha() for letter in string)

def capitalize_every_word(string: str) -> str:
    return " ".join([word.lower().capitalize() for word in split_string_by_words(string)])

def split_string_by_words(string: str, translate: bool = False) -> str | list[str]:
    return [cyrillic_to_latin_text(word) for word in string.split()] if translate else string.split()

def split_string_by_char(string: str, char: str) -> str:
    return string.split(char)

"""def is_any_close_match(text: str, similar_words: str | list[str]) -> bool:
    text_split = text.lower().replace("\n", " ").split(" ")

    if type(similar_words) == str:
        similar_words = string_to_list(similar_words)

    for similar_word in similar_words:
        if len(get_close_matches(similar_word, text_split, 1)) != 0:
            return True

    return False"""

"""def is_name_close(first_name: str, second_name: str) -> bool:
    similar_words = remove_close_matches(first_name, ["sekretar", "podpretsednik", "saopštava", "čita"])
    for similar_word in similar_words:
        first_name = first_name.lower().replace(f"{similar_word} ", "").replace(f" {similar_word}", "")

    if len(get_close_matches(first_name.lower(), [second_name.lower()], 1, 0.8)) != 0:
        return True
    elif len(get_close_matches("".join(first_name.lower().split(" ")[-2:]), [second_name.lower()], 1, 0.8)) != 0:
        return True

    return False"""

"""def remove_close_matches(text: str, similar_words: str | list[str]) -> str:
    similar_set, text_split = set(), text.lower().split(" ")

    if type(similar_words) == str:
        similar_words = string_to_list(similar_words)

    for similar_word in similar_words:
        for _close_match in get_close_matches(similar_word, text_split):
            similar_set.add(_close_match)

    return list(similar_set)

def capitalize_every_word(text: str):
    return " ".join([word.lower().capitalize() for word in text.split(" ")])

def without_words(similar_words: list[str], text: str) -> str:
    text_split = text.split(" ")

    for similar_word in similar_words:
        if len(get_close_matches(similar_word, text_split)) > 0:
            text_split.remove(similar_words)

    return " ".join(text_split)

def split_by_substring(string: str, substring: str, position: int = None) -> list[str]:
    if position is None:
        return string.split(substring)
    else:
        return string.split(substring, position)

def combine_substrings(*substrings: tuple[str]) -> str:
    return "".join([string for string in substrings])

def string_to_list(string: str):
    return [word.lower() for word in string.split(" ")]

def write_text(full_path: str, text: str) -> None:
    with open(full_path, "w") as f:
        f.write(text)

def get_text(path):
    with open(path, "r") as file:
        return to_latin(file.read(), "sr")"""

"""def text_with_bold(rows, previous_bold: bool = False) -> str:
    _string = StringIO()

    for row_element in rows:
        if row_element.is_bold:
            if not previous_bold:
                _string.write(f"[{row_element.text}")
            else:
                _string.write(row_element.text)
        else:
            if not previous_bold:
                _string.write(row_element.text)
            else:
                _string = _string[:-1]
                _string.write(f"] {row_element.text}")

    if "[" in _string and "]" not in _string:
        _string.write("]")

    return _string.getvalue()"""
