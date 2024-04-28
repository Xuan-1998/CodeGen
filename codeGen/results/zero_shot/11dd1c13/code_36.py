n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        dp[i][j] = max(grid[i-1][k]+abs(j-k) for k in range(n)) if grid[i-1][j] == 0 else grid[i-1][j]

print(min(dp[-1]))
