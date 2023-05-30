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
    return cyrillic_to_latin_text(string.replace("-\n", "").replace("\n", " ").replace("-", "").lower())

def is_close_match(string: str, string_list: str | list[str], threshold: int = 75, word_length: int = 3) -> bool:
    string_split = split_string_by_words(cyrillic_to_latin_text(string))

    if type(string_list) == str:
        return fuzz.ratio(string, string_list) >= threshold
    else:
        for word in [word for word in string_split if len(word) > word_length]:
            best_match, similarity = process.extractOne(word, string_list)
            if len(best_match) > word_length and similarity >= threshold:
                return True

        return False

def is_close_match_list(string: str, string_list: list[str], threshold: int = 75, word_min_length: int = 3) -> bool:
    for word in [word for word in split_string_by_words(only_normal_characters(string)) if len(word) > word_min_length]:
        best_match, similarity = process.extractOne(word, string_list)
        if len(best_match) > word_min_length and similarity >= threshold:
            return True
    return False

def is_close_match_string(string_one: str, string_two: str, threshold: int = 75) -> bool:
    if fuzz.ratio(only_normal_characters(string_one), only_normal_characters(string_two)) >= threshold:
        return True

def is_close_match_attendee(string_one: str, string_two: str, threshold: int = 75) -> bool:
    string_list, string_two = split_string_by_words(only_normal_characters(string_one)), \
        only_normal_characters(string_two)

    for i in range(len(string_list)):
        for j in range(len(string_list) - i):
            if fuzz.ratio(" ".join(string_list[j:i + j + 1]), string_two) >= threshold:
                return True
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
    close_matches = close_matches_to_remove(split_string_by_words(string, return_list=True), string_list)

    for word in close_matches:
        string = string.replace(f"{word} ", "").replace(f"{word}\n", "")

    return string

def closest_substring(first_string: str, second_string: str, treshold: int = 75) -> str:
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

def has_only_letters(string: str) -> bool:
    return all(letter.isalpha() for letter in string)

def capitalize_every_word(string: str) -> str:
    return " ".join([word.lower().capitalize() for word in split_string_by_words(string)])

def split_string_by_words(string: str, translate: bool = True, return_list: bool = True) -> str | list[str]:
    string_split = re.sub(r"(?<![A-Za-z])[\W_]|(?<=bw\.)\W", " ", string).split()

    if translate:
        string_split = [cyrillic_to_latin_text(word) for word in string_split]

    if return_list:
        return string_split

    return " ".join(string_split)
    # return [word for word in re.split(r"\s+|\n+|\t+", string) if word]

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
