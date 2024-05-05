import sys

# Read input from stdin
board = input().strip()
hand = input().strip()

# Initialize variables
removed_count = 0
inserted_count = 0
prev_color = None

# Loop through the board
for i, color in enumerate(board):
    # If the current ball is of the same color as the previous one,
    # increment removed_count and reset prev_color
    if color == prev_color:
        removed_count += 1
    else:
        prev_color = color
    
    # Check if there are three or more balls of the same color touching
    if i > 0 and board[i-1] == color and (i < len(board) - 1 and board[i+1] == color):
        removed_count += 3
        inserted_count += 1

# Calculate the minimum number of balls that need to be inserted
if removed_count + len(hand) >= len(board):
    print(-1)
else:
    print(min(len(hand), len(board) - removed_count))
