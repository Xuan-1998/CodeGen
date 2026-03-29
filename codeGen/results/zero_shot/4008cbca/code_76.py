import sys

def min_insertions(board, hand):
    # Convert board string to list for easier manipulation
    board = list(board)

    # Initialize count of removed balls and minimum insertions
    removed = 0
    min_inserts = 0

    # Loop until no more consecutive balls can be removed
    while True:
        # Check if there are three or more consecutive balls at the start
        i = 0
        while i < len(board) - 2 and board[i] == board[i+1] == board[i+2]:
            removed += 3
            board = board[i+3:]
            break

        # Check if there are three or more consecutive balls at the end
        j = 0
        while j < len(board) - 2 and board[-j-3] == board[-j-2] == board[-j-1]:
            removed += 3
            board = board[:-j-3]
            break

        # If no more consecutive balls can be removed, exit loop
        if i >= len(board) or j >= len(board):
            break

    # Calculate minimum insertions needed to remove all balls
    min_inserts = max(len(hand), len(board) - removed)

    return min_inserts

# Read input from stdin and print output to stdout
board = input()
hand = input()
print(min_insertions(board, hand))
