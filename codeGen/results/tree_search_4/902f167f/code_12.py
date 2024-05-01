def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base cases: empty rectangle or a rectangle with one side can't be tiled by any squares.
    for i in range(n + 1):
        dp[i][0] = 0
    for j in range(m + 1):
        dp[0][j] = 0

    # Calculate the minimum number of squares required to tile each sub-rectangle.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            min_squares = float('inf')
            for k in range(min(i, j) + 1):
                # Calculate the minimum number of squares required to tile the remaining sub-rectangle.
                min_squares = min(min_squares, dp[i - k][j - k] + 1)
            dp[i][j] = min_squares

    return dp[n][m]
