python
import sys
import bisect

def solve():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    
    index = 1
    for i in range(n):
        ai = int(data[index])
        bi = int(data[index + 1])
        points.append((ai, bi))
        index += 2
    
    # Sort points based on their positions
    points.sort()
    
    # Extract positions and ranges
    positions = [points[i][0] for i in range(n)]
    ranges = [points[i][1] for i in range(n)]
    
    # Initialize dp array
    dp = [0] * (n + 1)
    
    # Iterate from the second last point to the first point
    for i in range(n - 1, -1, -1):
        # Find the first position greater than ai + bi using binary search
        j = bisect.bisect_right(positions, positions[i] + ranges[i])
        if j == n:
            dp[i] = 1
        else:
            dp[i] = 1 + dp[j]
    
    # The result is the minimum number of points removed starting from the first point
    print(dp[0])


