#!/usr/bin/python3
def pascal_triangle(n):
    """
    Function that returns a pascal triangle

    Args:
        n: number of lines

    Returns:
        matrix: a matrix with the pascal triangle
    """

    matrix = []
    prev = []

    for i in range(n):
        res_list = []
        p = -1
        pn = 0

        for j in range(len(prev) + 1):
            if p == -1 or pn == len(prev):
                res_list += [1]
            else:
                res_list += [prev[p] + prev[pn]]

            p += 1
            pn += 1

        matrix.append(res_list)
        prev = res_list[:]

    return matrix
