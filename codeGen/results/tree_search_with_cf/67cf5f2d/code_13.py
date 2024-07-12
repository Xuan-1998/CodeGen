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
    
    # Step 1: Sort points by position
    points.sort()
    
    # Step 2: Initialize dp array
    dp = [0] * (n + 1)
    
    # Step 3: Process each point
    for i in range(1, n + 1):
        ai, bi = points[i - 1]
        dp[i] = i  # Worst case: remove all i points
        
        # Find the farthest point j that is not within the range of point i
        j = bisect.bisect_right(points, (ai - bi, float('inf'))) - 1
        
        if j >= 0:
            dp[i] = min(dp[i], dp[j + 1] + (i - j - 1))
        else:
            dp[i] = min(dp[i], i - 1)
    
    # The answer is the minimum number of points removed for all n points
    print(dp[n])

if __name__ == "__main__":
    main()

