def min_tiles(n, m):
    # Base case: single unit square
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][1] = i

    # Fill the dp table
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            if i <= j:
                dp[i][j] = min(dp[i-1][j], dp[i][j-i]) + 1
            else:
                dp[i][j] = dp[i][j-j] + 1

    return dp[n][m]

# Read input from stdin
n, m = map(int, input().split())

# Calculate the minimum number of squares
print(min_tiles(n, m))
