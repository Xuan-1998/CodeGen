import sys

def min_falling_path(grid):
    n = len(grid)
    dp = [[0] * (n + 1) for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(n):
            if i == n - 1:
                dp[i][j] = grid[i][j]
            else:
                dp[i][j] = max(dp[i + 1][:])
                dp[i][j] -= grid[i][j]

    return min(dp[0])

if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(min_falling_path(grid))
