import sys
from collections import deque

N = int(sys.stdin.readline())
grid = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]

dp = [[0] * N for _ in range(N)]
for i in range(N):
    dp[i][0] = grid[i][0]
    dp[0][i] = grid[0][i]

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(min(dp[-1]))
