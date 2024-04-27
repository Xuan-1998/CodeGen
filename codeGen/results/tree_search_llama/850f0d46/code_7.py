def chessboard_pattern(rows, cols):
    chessboard = {i: ['O'] * cols for i in range(1, rows+1)}
    
    for i in range(1, rows+1, 2):
        for j in range(1, cols+1, 2):
            chessboard[i][j-1] = 'X'
        for j in range(2, cols+1, 2):
            chessboard[i][j-1] = 'O' if chessboard[i][j-1] == 'X' else 'X'
    
    return '\n'.join([''.join(row) for row in chessboard.values()])

rows, cols = map(int, input().split())
print(chessboard_pattern(rows, cols))
