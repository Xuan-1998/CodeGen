def min_squares(n, m):
    # Initialize the memoization table with infinite values
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    # Base case: small rectangles can only be covered by one square
    for i in range(2, n + 1):
        dp[i][0] = 1
    for j in range(2, m + 1):
        dp[0][j] = 1

    # Fill the memoization table using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i < 2 or j < 2:
                dp[i][j] = 1
            else:
                min_val = float('inf')
                for k in range(1, min(i, j) + 1):
                    min_val = min(min_val, dp[i - k][j] + dp[k][j - k])
                dp[i][j] = min_val

    # Return the minimum number of squares needed to cover the original rectangle
    return dp[n][m]

# Example usage:
n, m = map(int, input().split())
print(min_squares(n, m))
