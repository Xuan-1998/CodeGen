def chessboard(rows, cols):
    board = [['X' if (i+j)%2 == 0 else 'O' for j in range(cols)] for i in range(rows)]
    return board

rows, cols = map(int, input().split())
for row in chessboard(rows, cols):
    print(' '.join(row))
