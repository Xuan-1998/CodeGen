def chessboard_pattern(rows, cols):
    board = [['O' if (i+j)%2 == 0 else 'X' for j in range(cols)] for i in range(rows)]
    for row in board:
        print(' '.join(row))

rows, cols = map(int, input().split())
chessboard_pattern(rows, cols)
