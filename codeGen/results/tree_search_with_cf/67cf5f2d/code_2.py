import sys
import bisect

def min_points_removed(n, points):
    points.sort()
    dp = [0] * (n + 1)
    
    for i in range(n - 1, -1, -1):
        pos, rng = points[i]
        farthest = pos - rng
        j = bisect.bisect_right(points, (farthest, float('inf'))) - 1
        dp[i] = min(dp[i + 1], dp[j + 1] + (i - j - 1))
    
    return dp[0]

if __name__ == '__main__':
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = [(int(data[2 * i + 1]), int(data[2 * i + 2])) for i in range(n)]
    
    result = min_points_removed(n, points)
    print(result)

