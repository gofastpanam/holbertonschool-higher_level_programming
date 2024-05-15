#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    difference_set_1 = set_1.difference(set_2)
    difference_set_2 = set_2.difference(set_1)
    difference_set_1.update(difference_set_2)
    return difference_set_1
