n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        dp[i][j] = max(grid[i-1][k] + grid[i][j] - grid[i-1][j] for k in range(n) if k != j)
print(max(dp[-1]))
