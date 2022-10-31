#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        counter = 0
        for i in sublist:
            if counter == (len(sublist) - 1):
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end=" ")
            counter += 1
        print("")
