def min_weight_triangulation(n):
    # Initialize the dynamic programming table
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # Base case is already covered since dp[i][i+1] = 0 for all i

    # Fill the DP table
    for length in range(2, n):  # length of the sub-polygon
        for i in range(1, n-length+1):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i+1, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + i*k*j)

    # The answer is the minimum weight triangulation of the full polygon
    return dp[1][n]

# Read input from standard input
n = int(input().strip())

# Output the answer to standard output
print(min_weight_triangulation(n))
