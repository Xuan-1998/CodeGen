from sys import stdin

def min_initial_points():
    N, M = map(int, stdin.readline().split())
    grid = []
    
    for _ in range(N):
        row = list(map(int, stdin.readline().split()))
        grid.append(row)

    dp = [[0] * (N) for _ in range(M)]
    max_points = [0] * N

    # Initialize the base case
    for j in range(N):
        dp[0][j] = grid[0][j]

    # Fill up the dynamic programming table
    for i in range(1, M):
        for j in range(N):
            if grid[i][j] > 0:
                max_points[j] = max(max_points[j], grid[i][j])
                dp[i][j] = max(0, min(dp[i-1][j], dp[i][j-1])) + max_points[j]

    return dp[-1][-1]

print(min_initial_points())
