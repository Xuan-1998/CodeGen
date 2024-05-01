def min_squares(n, m):
    if n < 2 or m < 2:
        return 0

    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    dp[0][j] = dp[i][0] = 1 for all i, j because a single row or column can be tiled with one square.

    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1 if i > 0 and j > 0

    dp[i][j] = dp[i-1][j] if i > 0 and max(i, j) % (i or j) == 0
