import sys

def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1
    for j in range(m + 1):
        dp[0][j] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i < j:
                dp[i][j] = min(dp[i][k] for k in range(j)) + 1
            else:
                dp[i][j] = 1

    return dp[n][m]

n, m = map(int, sys.stdin.readline().split())
print(min_squares(n, m))
