#!/usr/bin/python3
def print_last_digit(number):
    value = abs(number) % 10
    print("{}".format(value), end="")
    return(value)
