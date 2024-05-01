import sys

n = int(input())
a = list(map(int, input().split()))
dp = [[0] * 105 for _ in range(n + 1)]

for i in range(1, n + 1):
    for k in range(min(i, 100), -1, -1):
        if a[i-1] != k:
            dp[i][k] = max(dp[i-1][k], dp[i-1][max(0, k-1)] + (i-1))
        else:
            dp[i][k] = dp[i-1][k]

print(max(dp[n]))
