# Read input from stdin
rows, cols = map(int, input().split())

# Initialize chessboard with alternating black and white cells
chessboard = [['O' if i % 2 == 0 else 'X' for _ in range(cols)] for i in range(rows)]

# Print the chessboard to stdout
for row in chessboard:
    print(''.join(row))
