n, m, c0, d0 = map(int, input().split())
profit = [int(input()) for _ in range(m)]
dp = [[0] * (d0 + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(d0 + 1):
        if j < c0:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], profit[0] + (j - c0) // ci[0] * (di[0] - bi[0]))
            for k in range(1, m):
                if j >= ci[k]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - ci[k]] + profit[k] + (j - c0) // ci[k] * (di[k] - bi[k]))
            else:
                break
print(dp[n][d0])
