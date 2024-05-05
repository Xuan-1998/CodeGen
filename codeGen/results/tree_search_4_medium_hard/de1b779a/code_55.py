from sys import stdin

n, m, c0, d0 = map(int, stdin.readline().split())
dp = [[[0] * (m+1) for _ in range(n+1)] for _ in range(m+1)]

for i in range(1, n+1):
    for j in range(m+1):
        if i < c0:
            dp[j][i][0] = 0
        else:
            dp[j][i][0] = max(dp[j][i-1][0], dp[max(0, i-c0), j][k-1]) + d0

for i in range(1, n+1):
    for j in range(m+1):
        for k in range(1, min(i, m)+1):
            if i < ci[k]:
                dp[j][i][k] = 0
            else:
                dp[j][i][k] = max(dp[j][i-1][k], dp[max(0, i-ci[k]), j][k-1]) + di[k]

print(max([dp[i][m][k] for i in range(n+1) for k in range(m+1)]))
