import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())

# Initialize DP table with dimensions (14,14) to cover all possible inputs
dp = [[0] * 14 for _ in range(14)]

# Handle edge cases
for j in range(14):
    dp[0][j] = 1
for i in range(14):
    dp[i][0] = 1

# Fill up the DP table using the state expression
for i in range(1, n + 1):
    for j in range(1, m + 1):
        min_squares = sys.maxsize
        for k in range(min(i, j), 0, -1):
            if (i >= k and j >= k) or (k > 1 and dp[i-k][j-k] < min_squares):
                min_squares = min(min_squares, dp[i-k][j-k] + 1)
        dp[i][j] = min_squares

# Print the minimum number of integer-sided squares required to tile the given rectangle
print(dp[n-1][m-1])
