#!/usr/bin/python3
"""Find the peak value in a list"""


def find_peak(list_of_integers):
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    m = int(length / 2)
    l = list_of_integers

    if m - 1 < 0 and m + 1 >= length:
        return l[m]
    elif m - 1 < 0:
        return l[m] if l[m] > l[m + 1] else l[m + 1]
    elif m + 1 >= length:
        return l[m] if l[m] > l[m - 1] else l[m - 1]

    if l[m - 1] < l[m] > l[m + 1]:
        return l[m]

    if l[m + 1] > l[m - 1]:
        return find_peak(l[m:])
    return find_peak(l[:m])
