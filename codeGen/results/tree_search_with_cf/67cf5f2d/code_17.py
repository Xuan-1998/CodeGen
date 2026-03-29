import bisect

def minimize_removed_points(n, points):
    # Sort points by position
    points.sort()
    
    # Initialize dp array
    dp = [0] * (n + 1)
    
    # Iterate from the second-to-last point to the first point
    for i in range(n - 1, -1, -1):
        # Binary search to find the farthest point j to the left of i-th point
        j = bisect.bisect_left(points, (points[i][0] - points[i][1],)) - 1
        if j < 0:
            dp[i] = dp[i + 1] + 1
        else:
            dp[i] = min(dp[i + 1] + 1, dp[j + 1] + (i - j - 1))
    
    # The result is stored in dp[0]
    return dp[0]

# Read inputs
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
points = []
for i in range(n):
    ai = int(data[2 * i + 1])
    bi = int(data[2 * i + 2])
    points.append((ai, bi))

# Get the result
result = minimize_removed_points(n, points)

# Print the result
print(result)

