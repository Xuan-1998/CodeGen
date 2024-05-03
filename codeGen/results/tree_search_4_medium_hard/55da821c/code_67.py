===BEGIN CODE===
dp = [[0] * m for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i > 0:
            dp[i][j] = min(dp[i - 1][k] + (1 if k == s_i else 2) for k in range(1, m + 1))
        else:
            dp[i][j] = 0

print(sum([dp[-1][i] for i in range(1, m + 1)]))

===END CODE===
