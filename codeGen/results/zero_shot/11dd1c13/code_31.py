n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        dp[i][j] = grid[i][j] + min(dp[i-1][(j+1)%n], dp[i-1][j-1]) if j > 0 else grid[i][j]

print(min(dp[-1]))
