def min_operations(n, x):
    dp = [[float('inf')] * (10**(n-1) + 1) for _ in range(n+1)]

    # Base case: 0 operations needed to make length equal to 1
    for j in range(1, 10):
        dp[1][j] = 0

    # Fill in the dp table row by row
    for i in range(2, n+1):
        for j in range(10**(i-1), 10**i):
            for k in range(1, 10):
                if j * k < 10**i:
                    dp[i][j] = min(dp[i][j], dp[i-1][j*k] + 1)

    # Use the precomputed dp table values as lookups
    return dp[n][x] if x >= 10**(n-1) else -1

# Example usage
n, x = map(int, input().split())
print(min_operations(n, x))
