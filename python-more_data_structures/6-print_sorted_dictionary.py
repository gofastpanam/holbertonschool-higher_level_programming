#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    result = sorted(a_dictionary)
    for i in result:
        print("{}: {}".format(i, a_dictionary[i]))
