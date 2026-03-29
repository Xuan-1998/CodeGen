import sys

def solve(board, hand):
    # Initialize the result (minimum number of balls inserted)
    res = 0
    
    # Iterate through the board string
    i = 0
    while i < len(board):
        # Check if there are three or more same-colored balls in a row
        same_color = True
        count = 1
        while i + 1 < len(board) and board[i] == board[i+1]:
            i += 1
            count += 1
        
        # If not, insert a ball to break the sequence
        if count <= 2:
            res += 1
            i -= 1
        
        # Move on to the next position
        i += 1
    
    return res

# Read input from stdin
board = sys.stdin.readline().strip()
hand = sys.stdin.readline().strip()

# Solve the problem and print the result to stdout
print(solve(board, hand))
