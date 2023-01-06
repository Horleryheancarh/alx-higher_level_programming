#!/usr/bin/python3
def replace_in_list(list, i, elem):
    if i < 0:
        return list

    length = len(list)

    if i > length - 1:
        return list

    list[i] = elem

    return list
