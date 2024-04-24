def min_weight_triangulation(n):
    # Initialize the DP table with infinity
    dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    
    # Base case: The weight of a triangle is the product of its vertices
    for i in range(1, n-1):
        dp[i][i+2] = i * (i+1) * (i+2)
    
    # Fill the DP table
    for length in range(4, n+1):  # length of the sub-polygon
        for i in range(1, n-length+2):  # starting vertex
            j = i + length - 1  # ending vertex
            for k in range(i+1, j):  # vertex to form a triangle with i and j
                weight = i * j * k
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + weight)
    
    # The answer is the minimum weight triangulation of the full polygon
    return dp[1][n]

# Read the input from stdin
n = int(input().strip())

# Output the result
print(min_weight_triangulation(n))
