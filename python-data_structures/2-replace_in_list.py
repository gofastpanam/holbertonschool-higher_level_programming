#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for i, element in enumerate(my_list):
            new_element = (idx * 3)
            if idx == i:
                my_list[idx] = new_element
                return (my_list)
            if idx < 0:
                return (my_list)
            elif idx > len(my_list):
                return (my_list)

