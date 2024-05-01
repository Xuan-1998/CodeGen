import sys

def solve():
    n = int(input())
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1:
                dp[i][j] = max(grid[0][j], 0)
            elif j == 1:
                dp[i][j] = max(grid[i - 1][0], 0) + grid[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1] + grid[i][j], dp[i - 1][j]) + grid[i][j]

    return dp[n][n]

grid = []
for _ in range(int(input())):
    grid.append(list(map(int, input().split())))
print(solve())
