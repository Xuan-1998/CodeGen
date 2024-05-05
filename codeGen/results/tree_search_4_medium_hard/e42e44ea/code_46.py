===BEGIN CODE===
from sys import stdin
M, N = map(int, stdin.readline().split())
grid = [list(map(int, stdin.readline().split())) for _ in range(N)]

memo = [[float('inf') for _ in range(M)] for _ in range(N)]
memo[0][0] = grid[0][0]

for i in range(1, N):
    memo[i][0] = max(memo[i-1][0], 0) + grid[i][0]
for j in range(1, M):
    memo[0][j] = max(memo[0][j-1], 0) + grid[0][j]

for i in range(1, N):
    for j in range(1, M):
        if grid[i][j] > 0:
            memo[i][j] = min(memo[i-1][j], memo[i][j-1]) + grid[i][j]
        else:
            memo[i][j] = float('inf')

min_points = memo[N-1][M-1]

print(min_points)
===[END CODE]==
