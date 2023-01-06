#!/usr/bin/python3
def max_integer(list=[]):
    length = len(list)

    if length == 0:
        return None

    max = list[0]

    for i in range(1, length):
        if list[i] > max:
            max = list[i]

    return max
