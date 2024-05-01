def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i * i > j:
                dp[i][j] = 1
            else:
                for k in range(i, 0, -1):
                    for l in range(j, 0, -1):
                        if k * k <= l:
                            break
                    else:
                        continue
                    l += 1
                    dp[i][j] = min(dp[i][j], dp[k-1][l-1] + 1)
    
    return dp[n][m]
