# Read input from stdin
rows, cols = map(int, input().split())

# Initialize chessboard as a 2D list with empty strings
board = [['' for _ in range(cols)] for _ in range(rows)]

# Alternate between 'O' (white) and 'X' (black)
for i in range(rows):
    for j in range(cols):
        if (i + j) % 2 == 0:
            board[i][j] = 'O'
        else:
            board[i][j] = 'X'

# Print the chessboard pattern to stdout
for row in board:
    print(''.join(row))
