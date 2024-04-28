def count_paths(k, n, arr):
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]
    dp[0][0][0] = 1
    for i in range(1, n):
        dp[i][0][0] = dp[i-1][0][0]
        for j in range(1, n):
            dp[i][j][0] = dp[i-1][j][0] + dp[i][j-1][0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 0:
                for x in range(min(k, i), -1, -1):
                    for y in range(min(k, j), -1, -1):
                        dp[i][j][k] += dp[x-1][j][y]
    return dp[n-1][n-1][k]
