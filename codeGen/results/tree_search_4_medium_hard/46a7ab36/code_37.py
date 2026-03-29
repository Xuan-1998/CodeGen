n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n):
    dp[i][0] = 1
    for j in range(1, m + 1):
        if 2*i <= n:
            dp[i][j] = (dp[i-1][j-1] * len(alphabet) + 1) % (10**8 + 7)
        else:
            dp[i][j] = dp[i-1][j-1]

print(dp[n][m] % (10**8 + 7))
