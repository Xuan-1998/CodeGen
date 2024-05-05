import sys

def solve(board, hand):
    # Initialize the answer and the current streak
    ans = 0
    curr_streak = 1
    
    # Iterate through the board
    for i in range(1, len(board)):
        if board[i] == board[i-1]:
            curr_streak += 1
        else:
            curr_streak = 1
        
        # If we found a streak of three or more balls, remove it and increment the answer
        if curr_streak >= 3:
            ans += curr_streak - 2
            curr_streak = 1
    
    # Check if there are any remaining balls in the board that can't be removed
    for ball in board:
        if ball == 'R' or ball == 'Y' or ball == 'B' or ball == 'G':
            return -1
    
    return ans

# Read input from stdin
board = sys.stdin.readline().strip()
hand = sys.stdin.readline().strip()

# Print the answer to stdout
print(solve(board, hand))
