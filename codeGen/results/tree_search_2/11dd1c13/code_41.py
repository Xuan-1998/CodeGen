from sys import stdin

def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * (n + 1) for _ in range(n)]
    
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if i > 0:
                dp[i][j] = min(dp[i+1][k] for k in range(n) if k != j) + grid[i][j]
            else:
                dp[i][j] = grid[i][j]

    return min(dp[0])

grid = [list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]
print(min_falling_path_sum(grid))
