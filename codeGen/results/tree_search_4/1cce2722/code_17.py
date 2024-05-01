import sys

n = int(input())
a = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n):
    for j in range(i + 1):
        dp[i][j] = max(dp[i - 1][j], dp[i - 1][max(0, j - 1)] + (i + 1) - j)

print(dp[-1][-1])
