n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

dp = [[0] * n for _ in range(n)]
dp[0][0] = grid[0][0]
for i in range(1, n):
    dp[i][0] = min(dp[i-1][j]+grid[i][0] for j in range(n)) if i > 0 else grid[0][0]
    for j in range(1, n):
        dp[i][j] = min(max(dp[i-1][k-k+1]+grid[i][j] for k in range(j+1)), dp[i-1][j])
print(min(dp[-1]))
