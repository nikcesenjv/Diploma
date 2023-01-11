# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka convert_text_task.py

class ConvertTextTask:

    ALPHABET_CYRILLIC = "АаБбВвГгДдЂђЕеЖжЗзИиЈјКкЛлЉљМмНнЊњОоПпРрСсТтЋћУуФфХхЦцЧчЏџШш"
    ALPHABET_LATIN = "AaBbVvGgDdĐđEeŽžZzIiJjKkLlLjljMmNnNjnjOoPpRrSsTtĆćUuFfHhCcČčDždžŠš"
    def __init__(self, text):
        self.text = text

        self.converted_text = self.convert_text()

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def get_converted(self):
        return self.converted_text

    def convert_text(self):
        """res = ""
        for character in self.text:
            if character in self.ALPHABET_CYRILLIC:
                res += self.ALPHABET_LATIN[self.ALPHABET_CYRILLIC.index(character)]
            else:
                res += character
        return res"""

        return "".join([self.ALPHABET_LATIN[self.ALPHABET_CYRILLIC.index(character)]
                        if character in self.ALPHABET_CYRILLIC else character for character in self.text])