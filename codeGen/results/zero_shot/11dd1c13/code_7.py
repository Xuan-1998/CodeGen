n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][0] = grid[i][0]
    for j in range(1, n):
        dp[i][j] = min(dp[k][j-1] + grid[i][j] for k in range(min(i+1, n)))
print(min(max(row) for row in zip(*dp)))
