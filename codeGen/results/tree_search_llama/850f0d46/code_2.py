def generate_chessboard(rows, cols):
    chessboard = [['O' if (i+j)%2 == 0 else 'X' for j in range(cols)] for i in range(rows)]
    return '\n'.join([''.join(row) for row in chessboard])

rows, cols = map(int, input().split())
print(generate_chessboard(rows, cols))
