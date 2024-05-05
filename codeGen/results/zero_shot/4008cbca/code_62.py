import sys

def solve(board, hand):
    # Initialize the count of inserted balls
    inserted = 0
    
    # Iterate over the board and find the longest sequence of identical colors
    max_sequence = 0
    current_sequence = 1
    for i in range(len(board) - 1):
        if board[i] == board[i + 1]:
            current_sequence += 1
        else:
            max_sequence = max(max_sequence, current_sequence)
            current_sequence = 1
    
    # Calculate the remaining balls that need to be inserted
    remaining = len(board) - max_sequence * (max_sequence // 3 + 1)
    
    # Return the total count of inserted balls
    return inserted + remaining

# Read input from stdin
board = sys.stdin.readline().strip()
hand = sys.stdin.readline().strip()

# Print the output to stdout
print(solve(board, hand))
