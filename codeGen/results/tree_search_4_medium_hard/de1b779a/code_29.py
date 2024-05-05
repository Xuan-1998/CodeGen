from sys import stdin

n, m, c0, d0 = map(int, stdin.readline().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(m):
    ai, bi, ci, di = map(int, stdin.readline().split())
    for j in range(n, -1, -1):
        if j >= ci:
            dp[j][i] = max(dp[j-ci][i-1] + (j-ci)*di, dp[j][i-1] + bi*di)
        else:
            dp[j][i] = dp[j][i-1] + bi*di

print(max(dp[n]))
