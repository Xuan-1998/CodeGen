def min_squares(n, m):
    # Initialize the dp table with zeros
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 or j == 1:
                dp[i][j] = 1
            else:
                min_squares = float('inf')
                for k in range(min(i, j), 0, -1):
                    if i >= k and j >= k:
                        min_squares = min(min_squares, dp[i-k][j-k] + 1)
                dp[i][j] = min_squares

    return dp[n][m]

# Read the input from stdin
n, m = map(int, input().split())

print(min_squares(n, m))
