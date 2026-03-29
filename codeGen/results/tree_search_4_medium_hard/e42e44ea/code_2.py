def minInitialPoints(grid):
    n, m = len(grid), len(grid[0])
    dp = [[float('inf')] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                if i == 0 and j == 0:  # Top-left cell
                    dp[i][j] = grid[i][j]
                elif i > 0 and j > 0:  # Interior cells
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                elif i > 0:  # Cells only above the top-left cell
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                elif j > 0:  # Cells only to the right of the top-left cell
                    dp[i][j] = dp[i][j-1] + grid[i][j]

    return min(dp[-1][-1], float('inf')) - 1 if dp[-1][-1] != ∞ else -1

# Read input from stdin
n, m = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(n)]

print(minInitialPoints(grid))
