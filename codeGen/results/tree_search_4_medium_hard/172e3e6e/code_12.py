dp = [[0] * (n + 1) for _ in range(1000001)]
for i in range(2, n + 1):
    for j in range(i, 0, -1):
        if a[i-1] % j == 0:
            dp[j][i] += dp[j-1].count(j)
dp = sum(dp[n])

print(dp % (10**9 + 7))
