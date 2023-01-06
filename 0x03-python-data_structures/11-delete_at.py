#!/usr/bin/python3
def delete_at(list=[], i=0):
    length = len(list)

    if i < 0 or i >= length:
        return list

    del list[i]

    return list
