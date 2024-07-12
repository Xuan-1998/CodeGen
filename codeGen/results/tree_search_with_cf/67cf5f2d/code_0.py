python
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
    
    # Iterate from the second last point to the first point
    for i in range(n-1, -1, -1):
        ai, bi = points[i]
        # Find the farthest point j that can be removed when point i is activated
        j = bisect.bisect_right(points, (ai + bi, float('inf'))) - 1
        # Calculate dp[i]
        dp[i] = dp[j + 1] + (j - i)
    
    # The result is stored in dp[0]
    print(dp[0])

if __name__ == "__main__":
    main()

