dp = [[0] * (n + 2) for _ in range(n + 1)]
dp[0][j] = 1 if j == 0 else 0

for i in range(1, n + 1):
    dp[i][0] = dp[i-1][0]
    for j in range(min(i+1, n+2)):
        if j > 0:
            dp[i][j] = (dp[i-1][min(j, i)] +
                        sum(dp[k][min(l, k)] for k in range(min(i+1, j+1))))
        else:
            dp[i][j] = dp[i-1][j]

result = dp[n][n+1]
print(result % 998244353)
