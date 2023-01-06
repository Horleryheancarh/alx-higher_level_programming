#!/usr/bin/python3
def element_at(list, i):
    if i < 0:
        return None

    length = len(list)

    if i > length - 1:
        return None

    return list[i]
