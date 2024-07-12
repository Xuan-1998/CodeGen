python
import sys
import bisect

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    for i in range(n):
        ai = int(data[2 * i + 1])
        bi = int(data[2 * i + 2])
        points.append((ai, bi))
    
    # Sort points by their positions
    points.sort()
    
    # Extract the positions and ranges
    positions = [points[i][0] for i in range(n)]
    ranges = [points[i][1] for i in range(n)]
    
    # Initialize the dp array
    dp = [0] * (n + 1)
    
    # Iterate from the second last point to the first point
    for i in range(n - 1, -1, -1):
        # Find the rightmost point j that is within the range bi to the left of point i
        left_limit = positions[i] - ranges[i]
        j = bisect.bisect_right(positions, left_limit) - 1
        
        if j >= i:
            dp[i] = dp[i + 1]
        else:
            dp[i] = min(dp[i + 1], 1 + dp[j + 1])
    
    # The result is stored in dp[0]
    print(dp[0])

if __name__ == "__main__":
    main()

