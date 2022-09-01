#!/usr/bin/python3
"""
Module containing method to find whether all boxes
can be opened, contains function that returns bool
"""


def canUnlockAll(boxes):
    """Function to determine if boxes can be opened, returns with bool"""
    num_of_boxes = len(boxes)
    unlocked_boxes = [0]
    for el in boxes[0]:
        unlocked_boxes.append(el)
    
    for i in unlocked_boxes:
        for num in boxes[i]:
            if num < num_of_boxes and num not in unlocked_boxes:
                unlocked_boxes.append(num)
    
    for check in range(num_of_boxes):
        if check in unlocked_boxes:
            continue
        else:
            return False
    
    return True
