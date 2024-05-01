from math import inf

def min_squares(n, m):
    dp = [[inf] * (m + 1) for _ in range(n + 1)]
    dp[0][_] = 0 for _ in range(m + 1)
    dp[_][0] = 0 for _ in range(n + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i <= j:
                dp[i][j] = min(dp[max(0, i-k)][k] + 1 for k in range(j, -1, -1))
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][m]
