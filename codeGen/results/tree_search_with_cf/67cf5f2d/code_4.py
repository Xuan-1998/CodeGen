python
import sys
import bisect

def minimize_points_removed(n, points):
    # Sort points based on their positions
    points.sort()
    
    # Initialize DP array
    dp = [0] * (n + 1)
    
    # Initialize min_removed to a large value
    min_removed = float('inf')
    
    # Iterate from the second last point to the first point (right to left)
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        # Find the next point j such that ai + bi < aj using binary search
        j = bisect.bisect_right(points, (ai + bi, float('inf')))
        # Calculate dp[i]
        dp[i] = dp[j] + (j - i - 1)
        # Update min_removed
        min_removed = min(min_removed, dp[i])
    
    return min_removed

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    
    for i in range(n):
        ai = int(data[2 * i + 1])
        bi = int(data[2 * i + 2])
        points.append((ai, bi))
    
    result = minimize_points_removed(n, points)
    print(result)

