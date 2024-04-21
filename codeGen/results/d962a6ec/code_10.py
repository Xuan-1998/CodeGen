import sys
import math

def min_weight_triangulation(n):
    # Initialize the dp table
    dp = [[math.inf for _ in range(n)] for _ in range(n)]
    
    # Base cases: the weight of triangulating a polygon with two vertices is zero
    for i in range(n):
        dp[i][i] = 0
    
    # Calculate minimum weight for sub-polygons and store it in the dp table
    for length in range(2, n):  # length of the sub-polygon
        for i in range(n - length):  # start of the sub-polygon
            j = i + length  # end of the sub-polygon
            for k in range(i + 1, j):  # choose a vertex to triangulate
                weight = (i + 1) * (k + 1) * (j + 1)  # +1 because vertices are 1-based
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + weight)
    
    # Return the minimum weight of triangulating the entire polygon
    return dp[0][n - 1]

# Read input from stdin
n = int(sys.stdin.readline().strip())

# Output the answer to stdout
print(min_weight_triangulation(n))
