import sys

def solve(board, hand):
    # Initialize a set to store the removed colors
    removed_colors = set()

    while hand and board:
        # Find the first group of three or more balls that can be removed
        for i in range(len(board) - 2):
            if len(set(board[i:i+3])) == 1:  # Check if all three are the same color
                removed_colors.add(board[i])
                board = board[:i] + [''] * 3 + board[i+3:]
                break

        # If we didn't find a group to remove, it's not possible to remove all balls
        if not removed_colors:
            return -1

    # Calculate the minimum number of balls that need to be inserted
    min_insertions = len(hand) - sum(c in board for c in hand)
    return max(0, min_insertions)

# Read input from stdin and print output to stdout
board = sys.stdin.readline().strip()
hand = sys.stdin.readline().strip()

print(solve(board, hand))
