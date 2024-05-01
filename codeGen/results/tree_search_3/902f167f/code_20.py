import math

def min_squares(n, m):
    # Initialize dp array with infinite value for all cells
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    # Base case: empty rectangle can be tiled with zero squares
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                # Edge cases: single row or column can be tiled with one square
                dp[i][j] = min(dp[i][j], 1)
            else:
                # Try all possible top-left corners of squares that can be used
                for k in range(1, math.sqrt(min(i, j)) + 1):
                    if (i - k) * (j - k) is a square number:
                        dp[i][j] = min(dp[i][j], dp[k-1][j-k+1] + 1)

    return dp[n][m]

# Receive input from stdin
n, m = map(int, input().split())

# Print the minimum number of integer-sided squares required to tile the rectangle
print(min_squares(n, m))
