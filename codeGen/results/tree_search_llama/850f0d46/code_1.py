def chessboard_pattern(rows, cols):
    pattern = [['O' if (i + j) % 2 == 0 else 'X'
                for _ in range(cols)] for i in range(rows)]
    for row in pattern:
        print(' '.join(row))

rows, cols = map(int, input().split())
chessboard_pattern(rows, cols)
