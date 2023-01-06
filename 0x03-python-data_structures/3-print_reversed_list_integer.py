#!/usr/bin/python3
def print_reversed_list_integer(list=[]):
    if not list:
        pass
    else:
        list.reverse()
        for i in range(len(list)):
            print("{:d}".format(list[i]))
