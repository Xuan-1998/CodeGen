rows, cols = map(int, input().split())
board = [['O'] * cols for _ in range(rows)]

for i in range(1, rows, 2):
    for j in range(cols):
        board[i][j] = 'X'

for row in board:
    print(' '.join(row))
