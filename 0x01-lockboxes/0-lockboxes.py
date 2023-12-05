#!/usr/bin/python3


def canUnlockAll(boxes):
    """ determines whether all the boxes in a
    set of locked boxes can be opened"""
    if not boxes or len(boxes) == 0:
        return False
    keys = [0]
    visited_boxes = set(keys)
    while keys:
        current_box = keys.pop()
        for key in boxes[current_box]:
            if key < len(boxes) and key not in visited_boxes:
                visited_boxes.add(key)
                keys.append(key)
    return len(visited_boxes) == len(boxes)
