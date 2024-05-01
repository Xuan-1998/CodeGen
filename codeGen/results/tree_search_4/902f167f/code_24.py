def min_squares(n, m):
    # Initialize dp array
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    # Base case: dp[0][j] and dp[i][0]
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(n + 1):
        dp[i][0] = i

    # Fill up the dp table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            min_val = float('inf')
            for k in range(1, min(i, j) + 1):
                min_val = min(min_val, 1 + dp[i - k][j] if i >= k else 1 + dp[i][j - k])
            dp[i][j] = min_val

    # Return the minimum number of squares
    return dp[n][m]

n, m = map(int, input().split())
print(min_squares(n, m))
