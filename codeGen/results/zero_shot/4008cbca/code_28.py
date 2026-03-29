import sys

board = input().strip()
hand = input().strip()

def is_three_or_more_touching(board):
    # Check for sequences of three or more same color touching balls
    pass  # TO DO: implement this function

# Find and remove all sequences of three or more same color touching balls
while True:
    if not is_three_or_more_touching(board):
        break

# Try inserting balls from the hand to see if all the balls on the board can be removed
# This part will involve trying different combinations of ball insertions
