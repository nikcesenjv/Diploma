# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka archive_to_text_task.py

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

def archive_to_text_task(path, pages=None):
    resource_manager, file_handle = PDFResourceManager(), StringIO()
    converter = TextConverter(resource_manager, file_handle)
    interpreter = PDFPageInterpreter(resource_manager, converter)

    start, finish = get_pages_range(pages)

    with open(path, "rb") as file:
        for counter, page in enumerate(PDFPage.get_pages(file, caching=True, check_extractable=True)):
            if start <= counter + 1 <= finish:
                interpreter.process_page(page)

        text = file_handle.getvalue()
        converter.close()
        file_handle.close()

    if text:
        return text
    return None

def get_pages_range(pages):
    match len(pages):
        case 1:
            return pages[0], pages[0]
        case 2:
            return pages[0], pages[1]
        case _:
            return 1, 1000
