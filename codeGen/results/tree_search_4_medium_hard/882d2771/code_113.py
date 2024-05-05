import sys

t, l, r = map(int, input().split())

dp = [[0] * (r + 1) for _ in range(t + 1)]

for i in range(2, t + 1):
    for j in range(2, min(i, r) + 1):
        dp[i][j] = dp[i-1][min(j, i)] + (i > 1 and j > 1) * f(min(j, i)) % (10**9 + 7)

print(dp[t][r])
