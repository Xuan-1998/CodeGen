def generate_chessboard(rows, cols):
    chessboard = [['O' if i % 2 == 0 else 'X' for _ in range(cols)] for _ in range(rows)]
    return chessboard

rows, cols = map(int, input().split())
chessboard = generate_chessboard(rows, cols)

for row in chessboard:
    print(' '.join(row))
