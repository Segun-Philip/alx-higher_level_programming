#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy_dict = a_dictionary.copy()
    list_dict = list(copy_dict.keys())

    for i in list_dict:
        copy_dict[i] *= 2
    return (copy_dict)
