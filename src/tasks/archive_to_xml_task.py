# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka archive_to_xml_task.py

import zipfile
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

def archive_to_xml(path):
    doc = zipfile.ZipFile(path)
    print(doc.namelist())
    doc_xml = doc.read("word/document.xml")
    soup = BeautifulSoup(doc_xml, "xml")
    pretty = soup.prettify()

    print(pretty)

    """root = ET.fromstring(pretty)

    namespace = {'w': "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    body = root.findall(".//w:t", namespace)

    seznam = []

    for el in body:
        seznam.append(el.text)

    print("".join(seznam))"""




archive_to_xml("/Users/nikcesenjvodovnik/Documents/Programiranje/Diploma/lib/documents/word/19_1932_SKJ/18-40_redni/7_XXIV_SKJ_redni_14.4.1932.docx")
