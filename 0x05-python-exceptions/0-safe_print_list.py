#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    add = 0
    for i in range(x):
        try:
            adds = my_list[i]
            print("{}".format(adds), end="")
        except IndexError:
            break
        add += 1
    print("")
    return (add)

