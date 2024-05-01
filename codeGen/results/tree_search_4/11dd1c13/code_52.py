import sys

def min_falling_path(grid):
    n = len(grid)
    dp = [[0] * (n // 2 + 1) for _ in range(n)]

    dp[0][0] = grid[0][0]
    for i in range(1, n):
        for j in range(n // 2 + 1):
            if j % 2 == 0:
                k = j
            else:
                k = (j + 1) // 2
            dp[i][j] = min(dp[i-1][k], dp[i-1][(k+1)//2]) + grid[i][j]

    return min(dp[-1])

grid = [list(map(int, input().split())) for _ in range(int(input()))]
print(min_falling_path(grid))
