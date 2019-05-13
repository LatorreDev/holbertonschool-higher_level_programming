#!usr/bin/python3
def rotate_left_list(my_list=[], number_rotation=0):
    i = 0
    new_list = []
    idx = 0
    pos = number_rotation % len(my_list) - 1
    while i < len(my_list):
        new_list.append(my_list[i - pos])
        i += 1
    return new_list
