python
def minimize_removed_points(n, points):
    # Sort points based on their positions
    points.sort()
    
    # Initialize DP array
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # Iterate through points
    for i in range(1, n + 1):
        a_i, b_i = points[i - 1]
        # Find the farthest point that will be removed by this point
        j = i - 1
        while j >= 0 and points[j][0] >= a_i - b_i:
            j -= 1
        dp[i] = min(dp[i], dp[j + 1] + 1)
    
    # The result is the minimum value in the dp array considering the additional point
    return dp[n]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    points = []
    index = 1
    for _ in range(n):
        ai = int(data[index])
        bi = int(data[index + 1])
        points.append((ai, bi))
        index += 2
    
    result = minimize_removed_points(n, points)
    print(result)

