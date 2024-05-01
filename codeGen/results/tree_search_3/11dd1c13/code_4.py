import sys
from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][0] = grid[i][0]
for j in range(n):
    dp[0][j] = grid[0][j]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(dp[k][min(j-1, n-1)] + grid[i][j] for k in range(max(0, i-1)))

print(min(dp[-1]))
