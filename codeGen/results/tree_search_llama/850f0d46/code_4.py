def generate_chessboard(rows, cols):
    chessboard = []
    
    # Fill the first row with 'O'
    chessboard.append(['O'] * cols)
    
    for i in range(1, rows):
        # Alternate between 'O' and 'X'
        if i % 2 == 0:
            row = ['X'] + ['O' if j % 2 == 0 else 'X' for j in range(1, cols)]
        else:
            row = ['O'] + ['X' if j % 2 == 0 else 'O' for j in range(1, cols)]
        
        chessboard.append(row)
    
    return chessboard

# Read input from stdin
rows, cols = map(int, input().split())

# Generate and print the chessboard pattern
chessboard = generate_chessboard(rows, cols)
for row in chessboard:
    print(' '.join(row))
