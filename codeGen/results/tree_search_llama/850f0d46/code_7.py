rows, cols = map(int, input().split())
board = [['O' if (i+j) % 2 == 0 else 'X' for _ in range(cols)] for i in range(rows)]
for row in board:
    print(''.join(row))
