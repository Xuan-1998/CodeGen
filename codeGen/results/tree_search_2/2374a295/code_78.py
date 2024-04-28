import sys

n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(2, n + 1):
    for j in range(2, min(i, k) + 1):
        if i % j == 0:
            dp[i][j] = dp[i // j][j - 1] if j > 1 else 1
        else:
            dp[i][j] = 0

print((dp[n][k] % 1000000007) if k > 0 else 0)
