from sys import stdin

n = int(stdin.readline())

grid = []
for _ in range(n):
    row = list(map(int, stdin.readline().split()))
    grid.append(row)

dp = [[0] * len(grid[0]) for _ in range(len(grid))]

for i in range(1, n):
    for j in range(len(grid[0])):
        dp[i][j] = min(dp[i-1][k] + grid[i][j] for k in range(len(grid[0])))

print(min(dp[-1]))
