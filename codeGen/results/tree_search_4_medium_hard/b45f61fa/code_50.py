def minMultiplications(p):
    n = len(p)
    dp = [[0] * (n + 1) for _ in range(n)]

    # Base case: 0 multiplications needed to multiply no matrices
    dp[0][0] = 0

    for i in range(1, n):
        dp[i][i] = 0
        for j in range(i - 1, -1, -1):
            if j == i - 1:
                dp[j][i] = p[j] * p[j + 1] * p[i]
            else:
                dp[j][i] = float('inf')
                for k in range(j, i):
                    dp[j][i] = min(dp[j][i], dp[k][i] + p[j] * p[k + 1] * p[i])
        for j in range(i - 1, -1, -1):
            if j == i - 1:
                dp[0][j] = 0
            else:
                dp[0][j] = float('inf')
                for k in range(j + 1, i + 1):
                    dp[0][j] = min(dp[0][j], dp[0][k - 1] + p[j] * p[k] * p[i])

    return dp[0][-1]

# Example usage
p = [3, 2]
print(minMultiplications(p))  # Output: 6

