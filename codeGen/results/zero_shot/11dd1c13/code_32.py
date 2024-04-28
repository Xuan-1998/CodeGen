import sys
n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        dp[i][j] = max(grid[i-1][k] + (dp[k][j-1] if j > 0 else 0) for k in range(n)) - grid[i][j]
print(min(sum(row) for row in zip(*[col for col in dp])))
