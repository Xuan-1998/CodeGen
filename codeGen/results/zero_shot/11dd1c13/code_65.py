import sys
n = int(sys.stdin.readline())
grid = [list(map(int, line.split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(1, n):
    for j in range(n):
        dp[i][j] = grid[i][j] + min(dp[i-1][k] for k in range(n) if k != j)

print(min(dp[-1]))
