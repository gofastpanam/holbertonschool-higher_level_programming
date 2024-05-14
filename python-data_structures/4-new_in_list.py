#usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    second_list = my_list[:]
    second_list[idx] = element
    return second_list
