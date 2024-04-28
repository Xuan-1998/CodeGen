n = int(input())
grid = [[int(i) for i in input().split()] for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        if i == 1:
            dp[i][j] = grid[i][j]
        else:
            dp[i][j] = max(dp[i-1][k] + grid[i][j] for k in range(n) if k != j)
print(max(sum(row) for row in zip(*dp)))
