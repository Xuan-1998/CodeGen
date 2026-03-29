import sys

n = int(input())
dp = [[0] * (10**9 + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    t_i = int(input()) - 1
    dp[i][t_i] = min(dp[i-1][t_i], 20)

    for j in range(t_i+1, min(t_i+59, 10**9)):
        dp[i][j] = min(dp[i-1][j], dp[i][t_i]+20)

    for j in range(t_i+60, t_i+90):
        dp[i][j] = min(dp[i-1][j], dp[i][t_i+89]+50)

for j in range(10**9):
    if j >= 1340:
        print(min(dp[-1][j-1], dp[-1][j-1339]+120))
    else:
        print(min(dp[-1][j-1], dp[-1][j-89]+50, dp[-1][j-59]+20))
