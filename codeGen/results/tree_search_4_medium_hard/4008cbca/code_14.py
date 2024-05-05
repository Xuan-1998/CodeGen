import sys

def solve(board, hand):
    last_color = None
    dp = [0] * (len(board) + 1)
    
    for i in range(1, len(board) + 1):
        if board[i-1] == last_color:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + 1
        last_color = board[i-1]
    
    return dp[-1]

# Read input from stdin
board = sys.stdin.readline().strip()
hand = sys.stdin.readline().strip()

# Call the solver function
result = solve(board, hand)

# Print the result to stdout
print(result)
