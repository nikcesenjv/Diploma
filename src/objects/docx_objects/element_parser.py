# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka element_parser.py

class ElementParser:

    NAMESPACE = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    RULES = {"Style2": "head", "Style4": "text", "Style7": "head", "Style12": "note"}
    STYLES = {'Style2': 'CharStyle3', 'Style4': 'CharStyle5', 'Style7': 'CharStyle8', 'Style12': 'CharStyle13'}

    def get_rule(self, style: str) -> str:
        return self.RULES[style] if style is not None else None
