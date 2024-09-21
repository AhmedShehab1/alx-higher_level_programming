#!/usr/bin/python3
"""
Technical Interview Prep.
"""


def find_peak(list_of_integers):
    """
    finds the peak of a given list
    """
    if not list_of_integers:
        return None
    first = 0
    last = len(list_of_integers) - 1
    mid = (first + last) // 2
    while first <= last:
        current = list_of_integers[mid]
        if mid != 0 and mid != len(list_of_integers) - 1:
            if current >= list_of_integers[mid - 1]\
                    and current >= list_of_integers[mid + 1]:
                return current
            elif current < list_of_integers[mid - 1]:
                last = mid - 1
                mid = (first + last) // 2
            else:
                first = mid + 1
                mid = (first + last) // 2
        elif mid == 0:
            if current >= list_of_integers[mid + 1]:
                return current
        else:
            if current <= list_of_integers[mid - 1]:
                return current
