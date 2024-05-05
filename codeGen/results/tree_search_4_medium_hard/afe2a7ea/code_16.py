dp = [[0] * (n + 1) for _ in range(n + 2)]

for i in range(2, n + 2):
    for j in range(min(i, n)):
        dp[i][j] = (i-1)//2 * (1 if i > j else 1) + sum(dp[i-1][min(k, i-1)] for k in range(j+1))

print((dp[n][0] % (998244353)) - 1)
