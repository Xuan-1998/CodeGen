n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1,n):
    for j in range(n):
        if i == 1:
            dp[i][j] = grid[i][j]
        else:
            dp[i][j] = grid[i][j] + min(dp[i-1][k] for k in range(n) if k != j)

print(min(dp[-1]))
