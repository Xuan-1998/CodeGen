import sys
import bisect

def min_points_removed(n, points):
    # Sort the points based on their positions
    points.sort()
    
    # Initialize the dp array
    dp = [0] * (n + 1)
    
    # Iterate over each point
    for i in range(1, n + 1):
        a_i, b_i = points[i - 1]
        
        # Find the rightmost point j that will not be removed when point i is activated
        j = bisect.bisect_right(points, (a_i - b_i, float('inf'))) - 1
        
        # Update dp[i]
        dp[i] = min(dp[i - 1], dp[j + 1] + (i - j - 1))
    
    # The result is the minimum number of points removed when considering all points
    return dp[n]

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    index = 1
    for _ in range(n):
        a_i = int(data[index])
        b_i = int(data[index + 1])
        points.append((a_i, b_i))
        index += 2
    
    result = min_points_removed(n, points)
    print(result)

