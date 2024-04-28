def generate_chessboard(rows, cols):
    board = [['O'] if (i + j) % 2 == 0 else ['X'] for i in range(rows) for j in range(cols)]
    for row in board:
        print(' '.join(row))

rows, cols = map(int, input().split())
generate_chessboard(rows, cols)
