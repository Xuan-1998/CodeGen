from math import inf

def min_squares(n, m):
    dp = [[inf] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1
    for j in range(m + 1):
        dp[0][j] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i > 0 and j > 0:
                for k in range(min(i, j) + 1):
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + dp[k][j-1] + 1)

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
