import sys

def min_squares(n, m):
    # Create a 2D array dp with dimensions (n*m - n - m + 1) x (n*m - n - m + 1)
    dp = [[0] * (n*m - n - m + 1) for _ in range(n*m - n - m + 1)]

    # Fill the base cases: if there's only one row or column left, we need at most 1 square
    for i in range(1, n+1):
        dp[i-1][0] = 1
    for j in range(1, m+1):
        dp[0][j-1] = 1

    # Fill the DP table using the recurrence relation
    for i in range(1, n*m - n - m + 1):
        for j in range(1, n*m - n - m + 1):
            min_squares = sys.maxsize
            for k in range(1, min(i+1, n)+1):
                for l in range(1, min(j+1, m)+1):
                    if i-k >= 0 and j-l >= 0:
                        min_squares = min(min_squares, dp[i-k-1][j-l-1] + (k*l)**0.5)
            dp[i][j] = min_squares

    # The minimum number of squares required to tile the original rectangle is stored in dp[n*m-n-m+1-1][m-1]
    return int(dp[n*m-n-m+1-1][m-1])
