n, m, c0, d0 = map(int, input().split())
dp = [[[0 for _ in range(101)] for _ in range(11)] for _ in range(1001)]

for i in range(n+1):
    for j in range(m+1):
        for k in range(101):
            if i == 0:
                dp[i][j][k] = d0
            elif j == 0:
                dp[i][j][k] = max(dp[max(0, i-c0)][j-1][k], d0)
            else:
                dp[i][j][k] = max(dp[i-1][j-1][max(0, k-c0)] + d0, dp[max(0, i-c0)][j-1][k])

print(max(dp[n][m][k] for k in range(101)))
