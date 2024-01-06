#!/usr/bin/python3
""" Find a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    left = 0
    right = len(list_of_integers) - 1

    while left <= right:
        mid = left + (right - left) // 2
        cond1 = mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]
        cond2 = (mid == len(list_of_integers) - 1 or
                 list_of_integers[mid + 1] <= list_of_integers[mid])
        if cond1 and cond2:
            return list_of_integers[mid]
        if mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1
