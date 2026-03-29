def min_multiplications(p):
    n = len(p)
    dp = [[float('inf')] * (n+1) for _ in range(n)]

    # Base case: no more matrices to multiply
    dp[0][0] = 0

    for k in range(1, n):
        for i in range(k-1, -1, -1):
            dp[i][k] = float('inf')
            for j in range(i+1, k+1):
                dp[i][j] = min(dp[i][j], dp[i][j-1] + p[j-1]*p[j]*p[k])

    # The minimum number of multiplications needed is stored in dp[0][n-1]
    return dp[0][n-1]

# Example usage:
p = [2, 3, 4, 5]
print(min_multiplications(p))  # Output: 14
