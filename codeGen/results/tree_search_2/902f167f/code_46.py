def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 1
            elif i == 1:
                dp[i][j] = dp[i][j - 1] + 1
            elif j == 1:
                dp[i][j] = dp[i - 1][j] + 1
            else:
                min_val = float('inf')
                for k in range(1, i):
                    min_val = min(min_val, dp[k][j] + dp[i - k][j])
                dp[i][j] = min_val

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
