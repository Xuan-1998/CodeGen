n, m = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]
for j in range(m + 1):
    dp[0][j] = j

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = (dp[i - 1][j] + max(0, m - sum(dp[k][j] for k in range(i)))) % (10 ** 9 + 7)

print(dp[n][m])
