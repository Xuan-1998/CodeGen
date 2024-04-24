def min_weight_triangulation(n):
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Calculate the weight for each possible triangulation
    for length in range(2, n):  # length of the current sub-polygon
        for i in range(1, n-length+1):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i+1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + i*j*k)

    return dp[1][n]

# Read input from stdin
n = int(input().strip())

# Output the answer to stdout
print(min_weight_triangulation(n))
