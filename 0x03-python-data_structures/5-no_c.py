#!/usr/bin/python3
def no_c(str):
    length = len(str)

    j = 0

    n_str = str[:]

    for i in range(length):
        if (str[i] == 'c' or str[i] == 'C'):
            n_str = n_str[:(i - j)] + str[(i + 1):]
            j += 1

    return (n_str)
