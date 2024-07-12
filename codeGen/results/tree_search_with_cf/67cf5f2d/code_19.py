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
    
    # Sort points based on their positions
    points.sort()
    
    # Initialize dp array
    dp = [0] * (n + 1)
    
    # Iterate from the second-to-last point to the first point
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        # Find the farthest point j to the left that is not within the bi distance of the i-th point
        j = bisect.bisect_left(points, (ai - bi, -1)) - 1
        if j == -1:
            dp[i] = dp[i + 1] + 1
        else:
            dp[i] = min(dp[i + 1] + 1, dp[j + 1] + (i - j - 1))
    
    # The final answer is dp[0]
    print(dp[0])

if __name__ == "__main__":
    main()

