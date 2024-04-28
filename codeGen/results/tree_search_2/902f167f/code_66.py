def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1:
                dp[i][j] = j
            elif j == 1:
                dp[i][j] = i
            else:
                min_squares = float('inf')
                for k in range(1, int(min(i, j) ** 0.5) + 1):
                    if i >= k and j >= k:
                        min_squares = min(min_squares, dp[i - k][j] + dp[i][j - k] + 1)
                dp[i][j] = min_squares

    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
