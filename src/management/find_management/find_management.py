# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka find_management.py

def parse_find_params(params: list[str]) -> tuple[str, dict]:
    return params[0], {params[i]: params[i + 1] for i in range(1, len(params), 2)}
