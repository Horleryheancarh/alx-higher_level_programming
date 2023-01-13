#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    i = 0
    w = 0

    for tuple in my_list:
        i += tuple[0] * tuple[1]
        w += tuple[1]

    return i/w
