import sys

def min_falling_path(grid):
    dp = [[0] * len(grid[0]) for _ in range(len(grid))]

    for j in range(len(grid[0])):
        dp[0][j] = grid[0][j]

    for i in range(1, len(grid)):
        for j in range(len(grid[0])):
            if i > 0:
                dp[i][j] = min(dp[i-1][:j] + [grid[i][j]]) + grid[i][j]
            else:
                dp[i][j] = grid[i][j]

    return min(dp[-1])

if __name__ == "__main__":
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    print(min_falling_path(grid))
