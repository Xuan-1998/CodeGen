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
    
    # Initialize the dp array
    dp = [0] * (n + 1)
    
    # Iterate from the second last point to the first point
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        # Using binary search to find the first point j such that ai + bi < aj
        j = bisect.bisect_right(points, (ai + bi, float('inf')))
        dp[i] = dp[j] + 1
    
    # The result is the minimum value in the dp array
    result = min(dp)
    
    print(result)

if __name__ == "__main__":
    main()

