def safe_print_list_integers(my_list=[], x=0):
    add = 0
    for i in range(0, x):
        try:
            adds = my_list[i]
            print("{:d}".format(adds), end="")
        except (TypeError, ValueError):
            pass
        add += 1
    print("")
    return add
