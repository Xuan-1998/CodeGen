def print_chessboard():
    rows, cols = map(int, input().split())
    chessboard = [['X' if (i+j) % 2 else 'O' for j in range(cols)] for i in range(rows)]
    
    for row in chessboard:
        print(' '.join(row))

print_chessboard()
