import sys

n, m = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 or j == 1:
            dp[i][j] = 1
        else:
            min_squares = sys.maxsize
            for k in range(min(i, j), 0, -1):
                if (i % k) == 0 and (j % k) == 0:
                    min_squares = min(min_squares, dp[i // k][j // k] + 1)
            dp[i][j] = min_squares

print(dp[n][m])
