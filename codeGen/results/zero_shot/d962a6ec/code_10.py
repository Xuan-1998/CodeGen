def min_triangulation_weight(n):
    # Initialize a 2D list to store the minimum weight of a polygon from i to j
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    # Base case: triangles have a weight of 0 (no internal diagonals)
    for i in range(1, n+1):
        dp[i][i] = 0

    # Fill the DP table
    for length in range(2, n):  # length of the current polygon
        for i in range(1, n-length+1):
            j = i + length
            dp[i][j] = float('inf')  # Initialize with infinity
            for k in range(i+1, j):  # Place the diagonal between i and j
                # Weight of the triangle i-k-j plus the minimum weights of subpolygons
                weight = i * k * j + dp[i][k] + dp[k][j]
                dp[i][j] = min(dp[i][j], weight)

    return dp[1][n-1]  # The result is the minimum weight of the whole polygon

# Read the input
n = int(input().strip())

# Output the result
print(min_triangulation_weight(n))
