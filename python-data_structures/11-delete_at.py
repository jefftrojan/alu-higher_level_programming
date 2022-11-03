#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx <= 0:
        return my_list
    list_len = len(my_list)
    for i in range(list_len):
        if idx == my_list[i]:
            my_list.remove(i)
    return my_list
