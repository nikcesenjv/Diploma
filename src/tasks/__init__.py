# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka tasks/__init__.py

"""from .archive_to_text_task import ArchiveToTextTask
from .convert_numerals_task import ConvertNumeralsTask
from .convert_text_task import ConvertTextTask
from .file_parsing_task import FileParsingTask
from .find_objects_task import find_objects_task
# from .file_parsing_task import find_objects_task
from .logging_task import log
from .replace_directory_part_task import ReplaceDirectoryPartTask
from .retrieve_cer_task import RetrieveCERTask
# from .retrieve_directory_task import RetrieveDirectoryTask"""

from.archive_to_text_task import archive_to_text_task
from .convert_numerals_task import convert_numerals_task
from .directory_task import replace_directory_part_task, retrieve_directory_task
from .file_parsing_task import file_parsing_task
from .find_objects_task import find_objects_task
from .logging_task import log
from .retrieve_cer_task import retrieve_cer_task
