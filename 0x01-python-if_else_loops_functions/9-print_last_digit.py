#!/usr/bin/python3
def print_last_digit(i):
    if i >= 0:
        last_digit = i % 10
    else:
        last_digit = i % -10
        last_digit *= -1

    print(f"{last_digit:d}", end="")
    return last_digit
