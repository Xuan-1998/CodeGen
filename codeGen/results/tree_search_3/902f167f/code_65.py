from math import floor

def min_squares(n, m):
    # Initialize dp with base case values
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
    
    for j in range(m + 1):
        dp[0][j] = 1
    
    # Fill up the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            min_squares = float('inf')
            
            for k in range(i, -1, -1):
                if floor(i / k) * k >= j:
                    min_squares = min(min_squares, dp[k][j] + (i - k) // k)
            
            dp[i][j] = min_squares
    
    return dp[n][m]

# Read input from stdin
n, m = map(int, input().split())

print(min_squares(n, m))
