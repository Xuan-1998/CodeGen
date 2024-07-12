python
import sys
import bisect

def min_points_removed(n, points):
    # Sort points by their positions
    points.sort()
    
    # Initialize dp array
    dp = [0] * (n + 1)
    
    # Process points from right to left
    for i in range(n - 1, -1, -1):
        # Find the farthest point to the left that is not within bi distance of the i-th point
        pos_i, range_i = points[i]
        j = bisect.bisect_left(points, (pos_i - range_i, -float('inf')))
        
        # Update dp[i]
        dp[i] = min(dp[i + 1], dp[j] + (j - i))
    
    # The answer is dp[0]
    return dp[0]

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    
    for i in range(n):
        ai = int(data[2 * i + 1])
        bi = int(data[2 * i + 2])
        points.append((ai, bi))
    
    result = min_points_removed(n, points)
    print(result)

