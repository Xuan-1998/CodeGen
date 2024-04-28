n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
for i in range(1,n):
    for j in range(n):
        dp[i][j] = max(grid[i-1][k] for k in range(n) if abs(j-k)>0)+grid[i][j]
print(min(dp[-1]))
