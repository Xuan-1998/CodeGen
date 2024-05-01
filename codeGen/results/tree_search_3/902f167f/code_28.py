import sys

def min_squares(n, m):
    # Initialize dp table with infinity values
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    # Base case: For cells at the bottom or right edge of the rectangle, 
    # we can't place any more squares.
    for i in range(n + 1):
        dp[i][0] = 0
    for j in range(m + 1):
        dp[0][j] = 0
    
    # Fill up the dp table using dynamic programming and memoization
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            min_val = float('inf')
            for k in range(i):
                if (i - k) * (j - 1) > 0:
                    min_val = min(min_val, dp[k][j - 1] + 1)
            for m in range(j):
                if i * m > 0:
                    min_val = min(min_val, dp[i - 1][m] + 1)
            dp[i][j] = min_val
    
    return dp[n][m]

# Read input from standard input
n, m = map(int, sys.stdin.readline().split())

# Print the minimum number of squares required to tile the rectangle
print(min_squares(n, m))
