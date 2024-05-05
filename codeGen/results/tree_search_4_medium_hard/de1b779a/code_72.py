import sys

n, m, c0, d0 = map(int, input().split())

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = max(dp[max(0, i-c0)][0], 0) + d0

for j in range(1, m+1):
    ai, bi, ci, di = map(int, input().split())
    for i in range(c0, n+1):
        dp[i][j] = max(dp[max(0, i-ci)][j-1], dp[i-bi][j-1]) + di

print(max(dp[n]))
