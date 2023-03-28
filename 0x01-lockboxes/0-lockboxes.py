#!/usr/bin/python3
def canUnlockAll(boxes):
    # Create a list of boxes that are unlocked initially
    unlockedBoxes = [0]

    # Iterate through each key in each unlocked box
    for boxIndex in unlockedBoxes:
        for key in boxes[boxIndex]:
            # Add any new boxes that can be unlocked to the list of unlocked boxes
            if key not in unlockedBoxes and key < len(boxes):
                unlockedBoxes.append(key)

    # Return True if all boxes can be opened, else return False
    return len(unlockedBoxes) == len(boxes)
