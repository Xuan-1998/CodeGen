import sys

# Read input strings from stdin
board = list(sys.stdin.readline().strip())
hand = list(sys.stdin.readline().strip())

# Preprocess input data: convert strings to lists
board = [c for c in board]
hand = [c for c in hand]

# Identify danger areas in the board
danger_areas = []
for i in range(len(board) - 2):
    if board[i] == board[i+1] == board[i+2]:
        danger_areas.append((i, i+2))

# Calculate minimum number of inserts needed
inserts_needed = 0
for (start, end) in danger_areas:
    inserts_needed += end - start + 1

# Print the result to stdout
print(inserts_needed)
