import sys

# Read the input from stdin
board = list(sys.stdin.readline().strip())
hand = list(sys.stdin.readline().strip())

# Preprocess the board string
colors = {'R': 0, 'Y': 1, 'B': 2, 'G': 3, 'W': 4}
board_colors = [colors[c] for c in board]

def can_remove_all(board_colors, hand):
    # Check if there are any sequences of three or more same-colored balls
    for i in range(len(board_colors) - 2):
        if board_colors[i] == board_colors[i+1] == board_colors[i+2]:
            return False

    # Check if we have enough balls in the hand to remove all the remaining balls
    remaining_balls = sum(1 for c in board_colors if c != 0)
    if len(hand) < remaining_balls:
        return False

    return True

def min_insertions_to_remove_all(board_colors, hand):
    if not can_remove_all(board_colors, hand):
        return -1

    # Find the minimum number of balls that need to be inserted
    for i in range(len(hand)):
        remaining_hand = hand[:i] + hand[i+1:]
        if can_remove_all(board_colors, remaining_hand):
            return i + 1

    return -1

print(min_insertions_to_remove_all(board_colors, hand))
