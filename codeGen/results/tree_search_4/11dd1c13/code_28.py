import sys
from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    dp[i][0] = grid[i][0]
    visited[i][0] = True

for j in range(1, n):
    min_val = sys.maxsize
    for k in range(n):
        if not visited[0][k]:
            if dp[0][k] + grid[1][j] < min_val:
                min_val = dp[0][k] + grid[1][j]
                start_col = k
    for i in range(1, n):
        for j in range(n):
            if not visited[i][j]:
                if j != start_col:
                    dp[i][j] = min_val + grid[i][j]
                    visited[i][j] = True
                    if i == n - 1:
                        print(min(dp[-1]))
                        break
    for i in range(n):
        visited[i][0] = False

