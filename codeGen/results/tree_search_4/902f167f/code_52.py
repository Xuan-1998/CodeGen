from sys import stdin

def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            else:
                for k in range(min(i, j), 0, -1):
                    if (i - k) * (j - k) > 0 and (dp[i - k][j - k] + 1 < dp[i][j]):
                        dp[i][j] = min(dp[i][j], dp[i - k][j - k] + 1)
    return dp[n][m]

n, m = map(int, stdin.readline().split())
print(min_squares(n, m))
