import sys
import bisect

def main():
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
    
    # Initialize dp array
    dp = [0] * (n + 1)
    
    # Iterate from the n-1-th point to the 0-th point
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        # Find the farthest point j that will not be removed when point i is activated
        j = bisect.bisect_right(points, (ai + bi, float('inf'))) - 1
        dp[i] = min(dp[i + 1], 1 + dp[j + 1])
    
    # Output the result
    print(dp[0])

if __name__ == "__main__":
    main()

