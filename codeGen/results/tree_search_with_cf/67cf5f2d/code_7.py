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
    
    # Iterate from right to left
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        # Find the next point that is not affected by the current point's range
        j = bisect.bisect_right(points, (ai + bi, float('inf')))
        if j < n:
            dp[i] = dp[j] + 1
        else:
            dp[i] = 1
    
    # The answer is the minimum number of points removed starting from the leftmost point
    print(dp[0])

if __name__ == "__main__":
    main()

