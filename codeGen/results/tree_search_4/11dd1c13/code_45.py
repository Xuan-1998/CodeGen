import sys

def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * (n//2+1) for _ in range(n)]

    for j in range(n//2+1):
        dp[0][j] = grid[0][j]

    for i in range(1, n):
        for j in range(i//2+1):
            if j == 0:
                dp[i][j] = min(dp[i-1][:i//2]) + grid[i][j]
            elif j == i//2:
                dp[i][j] = min(dp[i-1][i//2:]) + grid[i][j]
            else:
                dp[i][j] = min([dp[i-1][k] for k in range(i//2)]) + grid[i][j]

    return min(dp[-1])

grid = [list(map(int, input().split())) for _ in range(int(input()))]
print(min_falling_path_sum(grid))
