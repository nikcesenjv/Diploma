# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka archive_to_text_task.py

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage

from .logging_task import LoggingTask as Log


class ArchiveToTextTask:
    def __init__(self, file):
        self.file = file

    def get_content(self, start=1, finish=-1):
        if finish == -1:
            finish = 1000

        resource_manager = PDFResourceManager()
        file_handle = StringIO()
        converter = TextConverter(resource_manager, file_handle)
        interpreter = PDFPageInterpreter(resource_manager, converter)

        with open(self.file.get_path(), "rb") as f:
            for site, page in enumerate(PDFPage.get_pages(f, caching=True, check_extractable=True)):
                if start <= site + 1 <= finish:
                    interpreter.process_page(page)

            text = file_handle.getvalue()

            converter.close()
            file_handle.close()

        if text:
            return text

        return None