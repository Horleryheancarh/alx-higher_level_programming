#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)

    if (len_s == 0):
        new_tup = (len_s, None)
    else:
        new_tup = (len_s, sentence[0])

    return new_tup
