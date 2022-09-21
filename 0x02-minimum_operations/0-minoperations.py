#!/usr/bin/python3
"""Module to write a method that calculates
the fewest number of operations needed to result
in exactly n H characters in the file"""


def minOperations(n):
    """Module to write a method that calculates
    the fewest number of operations needed to result
    in exactly n H characters in the file"""
    dict = {}
    el = 1
    for index in range(n + 1):
        el = el * 2
        dict[index + 1] = el
    for val in dict.items():
        if val[1] >= n:
            return val[0]