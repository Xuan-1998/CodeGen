rows, cols = map(int, input().split())
chessboard = [['O' if (i+j)%2 == 0 else 'X' for j in range(cols)] for i in range(rows)]

for row in chessboard:
    print(' '.join(row))
