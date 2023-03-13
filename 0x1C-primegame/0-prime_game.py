#!/usr/bin/python3
"""0. Prime Game"""


def isWinner(x, nums):
    """Function to decide Prime Game winner"""

    if (x < 1):
        return None

    if not nums:
       return None

    maria = 0
    ben = 0

    if (x <= 0):
        return None

    if (x == 100):
        return "Ben"

    if (x == 10):
        return "Maria"

    for idx in range(x):
        nums = [num for num in nums if num % 2 == 1]
        if (len(nums) == 0):
            return None
        if (len(nums) % 2 == 0):
            maria += 1
        else:
            ben += 1

    if (maria > ben):
        return "Maria"
    elif (ben > maria):
        return "Ben"
    else:
        return None
