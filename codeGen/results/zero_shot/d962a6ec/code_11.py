def min_weight_triangulation(n):
    # Initialize the dynamic programming table
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Base case: a triangle has no smaller triangulation
    for i in range(1, n+1):
        dp[i][i] = 0
    
    # Fill the DP table
    for length in range(2, n):  # length of the subpolygon
        for i in range(1, n-length+1):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i+1, j):
                weight = i * k * j
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + weight)
    
    return dp[1][n-1]

# Read input
n = int(input().strip())

# Get the minimum weight triangulation
result = min_weight_triangulation(n)

# Print the result
print(result)
