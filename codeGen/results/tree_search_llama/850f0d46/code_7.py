import sys

def generate_chessboard(rows, cols):
    # Pre-allocate the 2D array with alternating white and black cells
    chessboard = [['O' if (i + j) % 2 == 0 else 'X' for _ in range(cols)] 
                  for i in range(rows)]

    return chessboard

# Receive input from stdin
rows, cols = map(int, sys.stdin.readline().split())

# Generate the chessboard pattern
chessboard = generate_chessboard(rows, cols)

# Print the output to stdout
for row in chessboard:
    print(' '.join(row))
