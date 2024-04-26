# Read input row and column sizes from standard input
rows, cols = map(int, input().split())

# Initialize a 2D list (or array) with all cells set to 'O' (white)
chessboard = [['O'] * cols for _ in range(rows)]

# Alternate between 'O' (white) and 'X' (black) starting from the first row
for i in range(rows):
    if i % 2 == 0:  # even rows, start with 'O'
        chessboard[i] = ['O'] * cols
    else:
        chessboard[i] = ['X'] * cols

# Print the generated chessboard pattern to standard output
for row in chessboard:
    print(''.join(row))
