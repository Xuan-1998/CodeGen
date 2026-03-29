n = int(input())
dp = [[float('inf')] * (10000 // 60 + 1) for _ in range(101)]

for i in range(n):
    t_i = int(input()) - 1
    for j in range(10000 // 60 + 1):
        dp[i][j] = min(min(dp[i-1][max(0, j-1)] + 50, dp[i-1][j] + 20), dp[i-1][0] + 120)
    print(dp[i][t_i])
