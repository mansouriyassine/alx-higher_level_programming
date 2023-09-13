#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    result_list = list(map(lambda x: x * number, my_list))
    return result_list
