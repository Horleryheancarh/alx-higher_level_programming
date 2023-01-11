#!/usr/bin/python3
def subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            to_sub += n

    return max_list - to_sub

def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    rom_keys = list(rom.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for c in roman_string:
        for rom_num in rom_keys:
            if rom_num == c:
                if rom.get(c) <= last_rom:
                    num += subtract(list_num)
                    list_num = [rom.get(c)]
                else:
                    list_num.append(rom.get(c))

                last_rom = rom.get(c)

    num += subtract(list_num)

    return num
