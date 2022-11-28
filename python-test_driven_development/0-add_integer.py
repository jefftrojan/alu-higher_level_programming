#!/usr/bin/python3
""" Function that adds 2 integers """


def add_integer(a, b=98):
    return (a + b)
    if a or b != int or float:
        try:
            a = int(a)
            b = int(b)
        except TypeError:
            if a != int:
                print("a must be an integer")
            if b != int:
                print("b must be an integer")

