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
    
    # Process points from right to left
    for i in range(n - 1, -1, -1):
        ai, bi = points[i]
        # Find the next point that is not removed by the activation of point i
        next_point_index = bisect.bisect_right(points, (ai + bi, float('inf')))
        if next_point_index < n:
            dp[i] = dp[next_point_index] + 1
        else:
            dp[i] = 1  # No points to the right, only this point is removed

    # The answer is the minimum value considering adding the new point after the first or the second point
    result = min(dp[0], dp[1])

    print(result)

if __name__ == "__main__":
    main()

