#!/usr/bin/python3
def add_tuple(tup_a=(), tup_b=()):
    len_a = len(tup_a)
    len_b = len(tup_b)

    if len_a == 0:
        a1 = 0
        a2 = 0
    elif len_a == 1:
        a1 = tup_a[0]
        a2 = 0
    else:
        a1 = tup_a[0]
        a2 = tup_a[1]

    if len_b == 0:
        b1 = 0
        b2 = 0
    elif len_b == 1:
        b1 = tup_b[0]
        b2 = 0
    else:
        b1 = tup_b[0]
        b2 = tup_b[1]

    tup_c = (a1 + b1, a2 + b2)

    return tup_c
