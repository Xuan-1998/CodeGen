def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    hash_table = {}

    def is_square(k, m):
        return round(m**0.5) == k

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                for k in range(i):
                    for m in range(j):
                        if is_square(i - k, j - m):
                            dp[i][j] = min(dp[i][j], dp[k][m] + 1)

    return dp[n][m]
