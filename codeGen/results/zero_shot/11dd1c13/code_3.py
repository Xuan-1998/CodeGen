n = int(input())
grid = [[int(x) for x in input().split()] for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        dp[i][j] = max(grid[i-1][k] + (dp[i-1][k] if k != j else float('-inf')) for k in range(n))

print(min(dp[-1]))
