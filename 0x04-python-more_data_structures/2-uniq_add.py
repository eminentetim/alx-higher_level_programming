#!/usr/bin/python3
def uniq_add(my_list=[]):
    spc_list = set(my_list)
    num = 0

    for i in spc_list:
        num += i

    return (num)
