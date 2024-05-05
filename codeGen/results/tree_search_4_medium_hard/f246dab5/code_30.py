import sys

n = int(input())
dp = [[0] * 5 for _ in range(100010)]
for i in range(1, n+1):
    t_i = int(input())
    dp[t_i][2] += 50
    dp[t_i][4] += 120
    for j in range(3, -1, -1):
        for k in range(j-1, -1, -1):
            if dp[t_i][k]:
                dp[t_i][j] = min(dp[t_i][j], dp[t_i-k*90][k] + 50)
    print(sum([min(x, dp[i][2] + 20) for i in range(t_i+1)]))

