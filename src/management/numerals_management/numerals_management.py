# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka numerals_management.py

NUMERALS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}

def convert_numerals(num):
    if type(num) == str:
        return to_arab(num)
    else:
        return to_rim(num)

def to_arab(num):
    if num == "N":
        return 0

    if "." in num:
        num = num.split(".")
        "_".join([str(convert(n)) for n in num])
        return num

    return convert(num)


def convert(num):
    num_ar = 0
    for i in range(len(num)):
        if i > 0 and NUMERALS[num[i]] > NUMERALS[num[i - 1]]:
            num_ar += NUMERALS[num[i]] - 2 * NUMERALS[num[i - 1]]
        else:
            num_ar += NUMERALS[num[i]]

    return num_ar

# TODO: arab_to_rim()
def to_rim(num):
    return num
