import sys

M, N = map(int, input().split())
grid = [[int(x) for x in row.split()] for row in sys.stdin.readlines()]

dp = [[0] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        if grid[i][j] > 0:
            dp[i][j] = min(dp.get((i-1, j), [float('inf')]) + grid[i][j],
                           dp.get((i, j-1), [float('inf')]) + grid[i][j])

print(min(dp[-1][-1]))
