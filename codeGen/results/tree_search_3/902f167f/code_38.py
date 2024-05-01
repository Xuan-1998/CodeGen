def min_squares(n, m):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                dp[i][j] = 0
            elif i > 0 and j > 0:
                min_squares = float('inf')
                for k in range(i):
                    if (i - k) * (j - 1) ** 2 % (i - k) == 0:
                        min_squares = min(min_squares, dp[k][j - 1] + 1)
                for m in range(j):
                    if i * m ** 2 % i == 0:
                        min_squares = min(min_squares, dp[i - 1][m] + 1)
                dp[i][j] = min_squares
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
    
    return dp[n][m]

# Example usage:
n, m = map(int, input().split())
print(min_squares(n, m))
