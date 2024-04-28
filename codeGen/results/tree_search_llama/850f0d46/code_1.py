import sys

# Read input from stdin
rows, cols = map(int, sys.stdin.readline().split())

# Initialize the chessboard with all zeros (white)
chessboard = [[0] * cols for _ in range(rows)]

# Fill the chessboard using XOR
for i in range(rows):
    for j in range(cols):
        chessboard[i][j] = int((i + j) % 2 != 0)

# Print the chessboard to stdout
for row in chessboard:
    print(''.join(['O' if cell else 'X' for cell in row]))
