import sys

def min_weight_triangulation(n):
    # Initialize the dp table with 0's
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Base case: polygons with three vertices (single triangles)
    for i in range(1, n-1):
        dp[i][i+2] = i * (i+1) * (i+2)
    
    # Fill in the dp table for polygons with more than three vertices
    for length in range(3, n):
        for start in range(1, n-length+1):
            end = start + length
            dp[start][end] = float('inf')
            for mid in range(start+1, end):
                dp[start][end] = min(dp[start][end], dp[start][mid] + dp[mid][end] + start*end*mid)
    
    # Return the minimum weight for the entire polygon
    return dp[1][n]

# Read input from stdin
n = int(sys.stdin.readline().strip())

# Calculate and print the answer to stdout
print(min_weight_triangulation(n))
