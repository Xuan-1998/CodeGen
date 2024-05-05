import sys

def solve(board, hand):
    count = 0
    for i in range(len(board) - 2):  # Check each block of three balls
        if board[i] == board[i+1] == board[i+2]:
            count += 3
            continue  # Remove the current block and move on

    # Add any remaining balls that need to be inserted
    for color in hand:
        if color not in board:  # Check if the ball is not already in the row
            count += 1  # Increment the count by 1 for each additional ball

    return -1 if count < len(board) else count
