def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            else:
                min_squares = float('inf')
                for k in range(1, min(i, j) + 1):
                    min_squares = min(min_squares, dp[i-k][j] + dp[k][j-k])
                dp[i][j] = min_squares

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
