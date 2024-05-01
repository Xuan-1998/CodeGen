from sys import stdin

def solve():
    n, m = map(int, stdin.readline().split())
    grid = [list(map(int, stdin.readline().split())) for _ in range(n)]

    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(1, n):
        for j in range(m):
            if j == 0:
                dp[i][j] = min(grid[i-1][k] for k in range(m)) + grid[i][j]
            else:
                dp[i][j] = min(dp[i-1][k-1] + grid[i][k] for k in range(1, m)) or dp[i-1][j]

    return min(dp[-1])

print(solve())
