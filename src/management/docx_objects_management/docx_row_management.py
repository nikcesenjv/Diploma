# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka docx_row_management.py

import xml.etree.ElementTree as ET

def parse_docx_row_properties(row: ET, namespace: dict[str, str]) -> tuple[bool, str, int]:
    return is_row_bold(row, namespace), row_style(row, namespace), row_font_size(row, namespace)

def is_row_bold(row: ET, namespace: dict[str, str]) -> bool:
    return True if row.find(".//w:b", namespace) is not None else False

def row_style(row: ET, namespace: dict[str, str]) -> str:
    style_value = row.find(".//w:rStyle", namespace)
    return list(style_value.attrib.values())[0] if style_value is not None else None

def row_font_size(row: ET, namespace: dict[str, str]) -> int:
    font_size = row.find(".//w:sz", namespace)
    return int(list(font_size.attrib.values())[0]) / 2 if font_size is not None else None
