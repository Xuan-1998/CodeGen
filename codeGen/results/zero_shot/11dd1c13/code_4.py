n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        dp[i][j] = max(grid[i-1][k] + (dp[k][j] if k != j else 0) for k in range(n)) - min(grid[i-1][k] for k in range(n))
print(min(max(dp[i]) for i in range(n)))
