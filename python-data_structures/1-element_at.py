#!/usr/bin/python3
def element_at(my_list, idx):
    for i, element in enumerate(my_list):
        if idx == i:
            return(element)
    if idx > len(my_list):
        return(None)
    if idx < 0:
        return(None)
