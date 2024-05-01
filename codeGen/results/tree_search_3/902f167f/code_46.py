def min_tiles(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(min(i, j), 0, -1):
                if i >= k and j >= k:
                    dp[i][j] = min(dp[i][j], dp[i - k][j - k] + (i // k) * (j // k))
    return dp[n][m]

# Read input from stdin
n, m = map(int, input().split())

# Calculate and print the result to stdout
print(min_tiles(n, m))
