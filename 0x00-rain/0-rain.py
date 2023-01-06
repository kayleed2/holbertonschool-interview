#!/usr/bin/python3
"""
0_rain
"""


def rain(walls):
    """how much water is being retained by the walls"""
    if walls is None:
        return 0

    sum = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])
        sum = sum + (min(left, right) - walls[i])
    return sum
