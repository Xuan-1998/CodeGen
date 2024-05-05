def minInitialPoints(grid):
    m, n = len(grid), len(grid[0])
    dp = [[float('inf')] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0:
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                elif i > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                else: 
                    dp[i][j] = min([dp[0][k] for k in range(j)]) + grid[i][j]

    return dp[-1][-1]

N, M = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(N)]
print(minInitialPoints(grid))
