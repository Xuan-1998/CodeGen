def minInitialPoints(grid):
    N, M = len(grid), len(grid[0])
    dp = [[0] * M for _ in range(N)]

    # Base case: Top-left cell
    if grid[0][0] > 0:
        dp[0][0] = grid[0][0]
    else:
        return -1

    for i in range(1, N):
        for j in range(M):
            if j == 0 and grid[i][j] > 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
            elif i == 0 and grid[i][j] > 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
            else:
                dp[i][j] = min(dp[max(0, i-1)][j], dp[i][max(0, j-1)]) + grid[i][j]

    return dp[N-1][M-1]

# Example usage
N, M = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(N)]

result = minInitialPoints(grid)
print(result)
