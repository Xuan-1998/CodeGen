import sys

def find_min_insertions(board, hand):
    # Initialize a dictionary to keep track of the colors and their counts
    color_counts = {'R': 0, 'Y': 0, 'B': 0, 'G': 0, 'W': 0}

    # Count the colors in the board and hand
    for char in board + hand:
        if char in color_counts:
            color_counts[char] += 1

    # Calculate the minimum number of insertions needed to remove all the balls
    min_insertions = max(0, color_counts['R'] // 3 * 3)  # Remove R's in bulk
    for color, count in color_counts.items():
        if color != 'R':
            min_insertions += (count + 2) // 3  # Add the minimum number of insertions for each other color

    return -1 if min_insertions > len(hand) else min_insertions
