def chessboard_pattern(rows, cols):
    pattern = [['O' if (i + j) % 2 == 0 else 'X' 
                for j in range(cols)] 
               for i in range(rows)]
    
    # Print the board pattern
    for row in pattern:
        print(' '.join(row))

# Get input from stdin
rows, cols = map(int, input().split())

# Generate and print the chessboard pattern
chessboard_pattern(rows, cols)
