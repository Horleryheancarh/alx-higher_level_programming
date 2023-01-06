#!/usr/bin/python3
def new_in_list(list, i, elem):
    length = len(list)

    new_list = list[:]

    if 0 <= i < length:
        new_list[i] = elem

    return new_list
