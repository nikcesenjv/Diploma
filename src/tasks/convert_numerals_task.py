# Digitalizacija beležk SHS in Kraljevine Jugoslavije - Diplomsko delo
# Nik Česenj Vodovnik, 04180450 - Upravna informatika
# Študijsko leto 2022/2023
# Datoteka convert_numerals_task.py

"""class ConvertNumeralsTask:

    # NUMERALS CONVERSION RULES
    NUMERALS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}

    def __init__(self, num):
        self.num = num

    def rim_to_arab(self):
        if self.num == "N":
            return 0

        num_ar = 0
        for i in range(len(self.num)):
            if i > 0 and self.NUMERALS[self.num[i]] > self.NUMERALS[self.num[i - 1]]:
                num_ar += self.NUMERALS[self.num[i]] - 2 * self.NUMERALS[self.num[i - 1]]
            else:
                num_ar += self.NUMERALS[self.num[i]]

        return num_ar"""


NUMERALS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}

def convert_numerals_task(num):
    if type(num) == str:
        return to_arab(num)
    else:
        return to_rim(num)

def to_arab(num):
    if num == "N":
        return 0

    num_ar = 0
    for i in range(len(num)):
        if i > 0 and NUMERALS[num[i]] > NUMERALS[num[i - 1]]:
            num_ar += NUMERALS[num[i]] - 2 * NUMERALS[num[i - 1]]
        else:
            num_ar += NUMERALS[num[i]]

    return num_ar

def to_rim(num):
    return num
