#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0:
        newlist = my_list[:]
        return newlist
    elif idx >= length:
        newlist_2 = my_list[:]
        return newlist_2
    else:
        newlist_3 = my_list[:]
        newlist_3[idx] = element
        return (newlist_3)
