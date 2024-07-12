python
import sys
import bisect

def main():
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = [(int(data[2*i+1]), int(data[2*i+2])) for i in range(n)]
    
    # Sort points based on their positions
    points.sort()
    
    # Initialize dp array with infinity
    dp = [float('inf')] * (n + 1)
    dp[n] = 0  # No points to the right of the new point
    
    # Process points from right to left
    for i in range(n-1, -1, -1):
        ai, bi = points[i]
        # Find the first point j such that ai + bi < aj using binary search
        j = bisect.bisect_right(points, (ai + bi, float('inf')))
        dp[i] = dp[j] + 1
    
    # The answer is dp[0]
    print(dp[0])

if __name__ == "__main__":
    main()

