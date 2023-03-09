# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka parse_docx.py

import xml.etree.ElementTree as ET

from zipfile import ZipFile

import lxml
from bs4 import BeautifulSoup

def parse_docx(path):
    # document = ET.fromstring(ZipFile(path).read("word/document.xml"))

    namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    # paragraph_sections = document.find("w:body", namespace).findall("w:p", namespace)

    # body = document.find("w:body", namespace)
    # paragraph = body.findall("w:p", namespace)

    """for paragraph in paragraph_sections:
        text_e = paragraph.findall(".//w:t", namespace)
        seznam = []
        for t in text_e:
            seznam.append(t.text)
        print("".join(seznam))
        print()"""

    document = ZipFile(path).read("word/document.xml")
    root = ET.fromstring(document)

    body = root.find("w:body", namespace)
    paragraphs = body.findall("w:p", namespace)

    # section_labels = [get_section_text(s, namespace) if is_style2_section(s, namespace)
    #                   else "" for s in paragraphs]

    # print(section_labels)

"""def is_style2_section(p, namespace):
    return_val = False
    style_elem = p.find(".//w:pStyle[@w:val='Style2']", namespace)
    if style_elem is not None:
        return_val = True
    return return_val

def get_section_text(p, namespace):
    return_val = ""
    text_elem = p.findall(".//w:t", namespace)
    if text_elem is not None:
        return_val = "".join([t.text for t in text_elem])
    return return_val"""

def write_xml(path):
    doc = ZipFile(path)
    doc_xml = doc.read("word/document.xml")
    # print(doc_xml)
    soup = BeautifulSoup(doc_xml, "lxml").prettify()
    print(soup)

    """doc = ZipFile(path)
    doc_xml = doc.read("word/document.xml")
    soup = BeautifulSoup(doc_xml, "xml")
    pretty = soup.prettify()

    print(pretty)"""

"""doc = ZipFile(path).read("word/document.xml")
root = ET.fromstring(doc)

namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
body = root.find("w:body", namespace)
p_sections = body.findall("w:p", namespace)

for p in p_sections:
    text_e = p.findall(".//w:t", namespace)
    print("".join([t.text for t in text_e]))
    print()"""

"""doc = zipfile.ZipFile(path)
print(doc.namelist())
doc_xml = doc.read("word/document.xml")
soup = BeautifulSoup(doc_xml, "xml")
pretty = soup.prettify()

print(pretty)

root = ET.fromstring(pretty)

namespace = {'w': "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
body = root.findall(".//w:t", namespace)

seznam = []

for el in body:
    seznam.append(el.text)

print("".join(seznam))"""

parse_docx("/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/lib/documents/word/19_1932_SKJ/18-40_redni/7_XXIV_SKJ_redni_14.4.1932.docx")