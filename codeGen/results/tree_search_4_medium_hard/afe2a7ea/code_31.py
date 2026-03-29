m = 998244353

n = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = 1
    for j in range(min(i, n)):
        if i > 1:
            dp[i][j + 1] = (sum(dp[i - 1][k] for k in range(min(j + 1, n))) % m)
        else:
            dp[i][j + 1] = 1

print((dp[n][0] % m) * pow(m - 1, -1, m))
