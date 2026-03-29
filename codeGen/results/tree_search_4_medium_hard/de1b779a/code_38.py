import sys

n, m, c0, d0 = map(int, input().split())
dp = [[[-1] * 101 for _ in range(101)] for _ in range(m + 1)]

for i in range(m + 1):
    ai, bi, ci, di = map(int, input().split())
    dp[i][c0][c0 == d0] = 0

for i in range(m, -1, -1):
    for j in range(n, -1, -1):
        for k in [False, True]:
            if c0 <= j and (not k or ai >= bi):
                dp[i][j][k] = max(dp[i-1][j-ci[k]][!k] + di[k], dp[i-1][j][k])
            else:
                dp[i][j][k] = dp[i-1][j][k]

print(max(max(map(max, dp))))

