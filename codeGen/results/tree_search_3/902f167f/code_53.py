def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            elif i > 0 and j > 0:
                dp[i][j] = min((i * (i - 1)) // 2 + (j * (j - 1)) // 2, 
                               dp[max(0, i - int(i ** 0.5))][max(0, j - int(j ** 0.5))] + 
                               ((i - int(i ** 0.5)) * (i - int(i ** 0.5))) // 2 +
                               ((j - int(j ** 0.5)) * (j - int(j ** 0.5))) // 2)
            else:
                dp[i][j] = max(dp[max(0, i - 1)][j], dp[i][max(0, j - 1)])

    return dp[n][m]
