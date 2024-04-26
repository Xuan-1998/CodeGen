def generate_chessboard(rows, cols):
    board = [['O' if (i + j) % 2 == 0 else 'X'
              for _ in range(cols)] 
             for i in range(rows)]
    return board

rows, cols = map(int, input().split())
for row in generate_chessboard(rows, cols):
    print(' '.join(row))
