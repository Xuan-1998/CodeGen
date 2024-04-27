def generate_chessboard(rows, cols):
    # Initialize the chessboard with all white cells
    board = [['O' for _ in range(cols)] for _ in range(rows)]

    # Alternate between black and white cells starting from the first row
    for i in range(rows):
        for j in range(cols):
            if (i + j) % 2 == 0:
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'

    # Print the chessboard pattern
    for row in board:
        print(' '.join(row))

# Read input from stdin and generate the chessboard
rows, cols = map(int, input().split())
generate_chessboard(rows, cols)
