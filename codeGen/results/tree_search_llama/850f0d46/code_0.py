rows, cols = map(int, input().split())

# Initialize the chessboard with all white cells ('O')
chessboard = [['O' for _ in range(cols)] for _ in range(rows)]

for row in range(rows):
    for col in range(cols):
        if (row + col) % 2 == 1:  # If the sum of row and column indices is odd, mark as black ('X')
            chessboard[row][col] = 'X'

# Print the generated chessboard
for row in chessboard:
    print(' '.join(row))
