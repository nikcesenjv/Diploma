# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka paragraph.py

class Paragraph:
    def __init__(self, content):
        self.content = content

    @property
    def paragraph_style(self):
        return self.content
