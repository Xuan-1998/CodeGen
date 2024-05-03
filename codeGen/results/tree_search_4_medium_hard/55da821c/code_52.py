import sys

def min_replant(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        s_i, x_i = int(sys.stdin.readline()), float(sys.stdin.readline())
        for j in range(1, min(i, m) + 1):
            if dp[i - 1][j] > 0:
                continue
            if (x_i >= dp[i - 1][j - 1][-1] and s_i == dp[i - 1][j - 1].get(-1, 0)):
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1][s_i - 1] + (i > j))
            else:
                dp[i][j] = min(dp[i][j], dp[i - 1][j][s_i - 1] + (i > j))
    return dp[-1][-1]

n, m = map(int, sys.stdin.readline().split())
print(min_replant(n, m))
