import sys

def min_initial_points(grid):
    n, m = len(grid), len(grid[0])
    dp = [[0] * m for _ in range(n)]
    
    # Base cases: initial points required to reach top or left cells
    for j in range(m):
        dp[0][j] = grid[0][j]
    for i in range(n):
        dp[i][0] = grid[i][0]

    # Recurrence relation: minimum initial points required to reach current cell
    for i in range(1, n):
        for j in range(1, m):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    # Return the minimum initial points required to reach bottom-right cell
    return dp[-1][-1]

if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(min_initial_points(grid))
