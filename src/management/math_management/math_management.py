# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka math_management.py

def average(values_list: list[int | float], preffered_round: int = 2, percent: bool = True) -> float:
    result = sum(values_list) / len(values_list)

    if percent:
        result *= 100

    return round(result, preffered_round)
