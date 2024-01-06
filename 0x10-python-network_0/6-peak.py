#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers."""


def find_a_peak(numbers):
    """Recursively find a peak element"""
    if not numbers:
        return None
    return peak_helper(numbers, 0, len(numbers) - 1)


def peak_helper(nums, start, end):
    """Helper function for finding the peak recursively"""
    if start == end:
        return nums[start]
    if end - start == 1:
        return max(nums[end], nums[start])
    mid = (start + end) // 2
    if nums[mid] < nums[mid + 1]:
        return peak_helper(nums, mid + 1, end)
    return peak_helper(nums, start, mid)


def find_peak(list_of_integers):
    """Function to find a peak in a list"""
    return find_a_peak(list_of_integers)
