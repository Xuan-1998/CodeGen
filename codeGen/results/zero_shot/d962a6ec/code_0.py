def min_weight_triangulation(n):
    # Initialize the DP table with infinity
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    
    # Base case: A triangle has zero weight of triangulation
    for i in range(1, n+1):
        dp[i][i] = 0
        if i < n:
            dp[i][i+1] = 0
    
    # Fill the DP table
    for length in range(2, n):
        for i in range(1, n-length+1):
            j = i + length
            for k in range(i+1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + i*k*j)
    
    # The answer is the minimum weight of triangulating the whole polygon
    return dp[1][n]

# Read input from stdin
n = int(input().strip())

# Print the answer to stdout
print(min_weight_triangulation(n))
