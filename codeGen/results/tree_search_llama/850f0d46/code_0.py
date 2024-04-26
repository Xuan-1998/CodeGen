rows, columns = map(int, input().split())
board = [['O'] if i % 2 == 0 else ['X'] for i in range(rows)]

for row in board:
    print(' '.join(row))
