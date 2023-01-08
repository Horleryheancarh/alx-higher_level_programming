#!/usr/bin/python3
def divisible_by_2(list=[]):
    divisible = []

    for i in range(len(list)):
        if list[i] % 2 == 0:
            divisible.append(True)
        else:
            divisible.append(False)

    return divisible
