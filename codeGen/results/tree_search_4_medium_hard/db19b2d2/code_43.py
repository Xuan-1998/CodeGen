import sys

n, m, h = map(int, input().split())
s = [int(x) for x in input().split()]

dp = [[0.0] * (h+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = 1 - (1 - s[h-1]/sum(s)) ** (n-i)
    for j in range(1, h+1):
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1] * s[h-1]/sum(s)

print(sum(dp[n][i] for i in range(h, n+1)))
