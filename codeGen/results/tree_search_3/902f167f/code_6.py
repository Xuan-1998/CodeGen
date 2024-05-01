def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if min(i, j) == 1:
                dp[i][j] = 1
            elif i > 0 and j > 0:
                min_value = float('inf')
                for k in range(1, min(i, j) + 1):
                    min_value = min(min_value, dp[max(0, i-k)][max(0, j-k)] + 1)
                dp[i][j] = min_value
            else:
                dp[i][j] = 0

    return dp[n-1][m-1]
