#!/usr/bin/python3
def print_matrix_integer(list=[[]]):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if j != 0:
                print(" ", end="")
            print("{:d}".format(list[i][j]), end="")
        print()
