===BEGIN CODE===
def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    # Base case: A single row or column can be tiled with one square
    for j in range(m + 1):
        dp[0][j] = 1
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill up the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            min_val = float('inf')
            for k in range(min(i, j) + 1):
                min_val = min(min_val, (i - k) * (j - k) + dp[k][k])
            dp[i][j] = min_val

    # The minimum number of squares required to tile the rectangle
    return dp[n][m]

===END CODE===
