def min_weight_triangulation(n):
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Base cases are already initialized to 0

    # Fill dp table
    for length in range(3, n+1):  # length of the sub-polygon
        for i in range(1, n-length+2):  # starting vertex of the sub-polygon
            j = i + length - 1  # ending vertex of the sub-polygon
            dp[i][j] = float('inf')  # Initialize with infinity
            
            # Find minimum weight triangulation for sub-polygon [i, j]
            for k in range(i+1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + i*j*k)

    # Return the minimum weight triangulation for the full polygon
    return dp[1][n]

# Read input from stdin
n = int(input().strip())

# Output the answer to stdout
print(min_weight_triangulation(n))
