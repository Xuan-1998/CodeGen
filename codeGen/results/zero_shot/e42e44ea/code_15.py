def minInitialPoints(grid):
    N, M = len(grid), len(grid[0])
    dp = [[0] * (M+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            if grid[i-1][j-1] > 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
    
    return dp[N][M]

# Read input from stdin
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

print(minInitialPoints(grid))
