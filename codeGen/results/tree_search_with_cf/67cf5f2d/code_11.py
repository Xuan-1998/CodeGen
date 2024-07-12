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
    
    # Initialize dp array
    dp = [0] * (n + 1)
    
    # Process points from right to left
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        # Find the first point that is not removed by the i-th point
        j = bisect.bisect_right(points, (ai - bi, float('inf'))) - 1
        dp[i] = dp[i + 1] + 1  # If we don't add the new point, we remove this point
        if j >= 0:
            dp[i] = min(dp[i], dp[j + 1])
    
    # The result is the minimum number of points removed
    print(dp[0])

if __name__ == "__main__":
    main()

