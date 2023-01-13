#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    l_keys = list(a_dictionary.keys())

    for cur_value in l_keys:
        if value == a_dictionary.get(cur_value):
            del a_dictionary[cur_value]

    return a_dictionary
