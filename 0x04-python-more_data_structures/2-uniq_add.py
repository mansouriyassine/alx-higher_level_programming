#!/usr/bin/python3

def uniq_add(my_list=[]):
    u, s = set(), 0
    [u.add(n) for n in my_list if n not in u or u.add(n)]
    return sum(u)
