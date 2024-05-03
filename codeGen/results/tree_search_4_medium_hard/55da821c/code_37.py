def min_replanting(n, m):
    dp = [[float('inf')] * (n + 1) for _ in range(m)]
    dp[0][0] = 0

    for i in range(1, m):
        for j in range(i):
            for k in range(j + 1):
                if k == i - 1:
                    dp[i][j] = min(dp[i][j], dp[j][k])
                else:
                    dp[i][j] = min(dp[i][j], dp[j][k] + (j - k))

    return dp[m - 1][n]

n, m = map(int, input().split())
print(min_replanting(n, m))
