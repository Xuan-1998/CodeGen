import sys

n, m, c0, d0 = map(int, input().split())
dp = [[[0] * (m+1) for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if i < c0:
            dp[i][j][0] = 0
        else:
            dp[i][c0][0] = d0

for i in range(m+1):
    for j in range(n+1):
        for k in range(max(0, j-ci)):
            if i > 0 and k > 0:
                dp[i][j][k] = max(dp[max(0, i-c0)][j-1][0], dp[i][j][k-1] + d0)
            elif k == 0:
                dp[i][j][k] = dp[max(0, i-ci)][j-1][0]
print(max(dp[m][n]))
