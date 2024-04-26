rows, cols = map(int, input().split())

chess_board = [['O' if (i+j)%2 == 0 else 'X' for j in range(cols)] for i in range(rows)]

for row in chess_board:
    print(' '.join(row))
