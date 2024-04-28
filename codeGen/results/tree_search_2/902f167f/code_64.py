def min_squares(n, m):
    max_size = max(n, m)
    dp = [[float('inf')] * (max_size + 1) for _ in range(max_size + 1)]

    for i in range(1, max_size + 1):
        for j in range(1, max_size + 1):
            if i == 1 or j == 1:
                dp[i][j] = 0
            else:
                min_squares = float('inf')
                for k in range(1, min(i, i + j) + 1):
                    min_squares = min(min_squares, dp[k - 1][k] if i >= k and j >= k else 0)
                dp[i][j] = min_squares

    return dp[n][m]

# Example usage
n = int(input())
m = int(input())
print(min_squares(n, m))
