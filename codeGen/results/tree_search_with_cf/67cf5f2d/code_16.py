python
def minimize_removed_points(n, points):
    # Sort points by their coordinate
    points.sort()

    # dp[i] will store the minimum number of points removed considering the first i points
    dp = [float('inf')] * n
    dp[0] = 0  # Base case: no points removed if there's only one point

    for i in range(1, n):
        dp[i] = dp[i - 1]  # At worst, we remove the current point

        # Check all previous points
        for j in range(i - 1, -1, -1):
            if points[j][0] >= points[i][0] - points[i][1]:
                dp[i] = min(dp[i], dp[j] + 1)
            else:
                break

    # The result is the minimum value in dp array after considering all points
    return min(dp)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    for i in range(n):
        ai = int(data[2 * i + 1])
        bi = int(data[2 * i + 2])
        points.append((ai, bi))
    
    result = minimize_removed_points(n, points)
    print(result)

