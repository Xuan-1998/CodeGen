n, m = map(int, input().split())
dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        for k in range(i, -1, -1):
            for l in range(j, -1, -1):
                if (k * k) <= i and (l * l) <= j:
                    dp[i][j] = min(dp[i][j], dp[k][l] + 1)
print(dp[n][m])
