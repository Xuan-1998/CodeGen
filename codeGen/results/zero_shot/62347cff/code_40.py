import sys
from collections import deque

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    queue = deque([(0, 0)])
    while queue:
        i, j = queue.popleft()
        if i == m - 1 and j == n - 1:
            break
        for dx in [-1, 0, 1]:
            ni, nj = i + dx, j
            if 0 <= ni < m and 0 <= nj < n:
                new_sum = dp[i][j] + grid[ni][nj]
                if ni == 0 or nj == 0 or (ni > 0 and nj > 0 and dp[ni-1][nj-1] < new_sum):
                    continue
                dp[ni][nj] = new_sum
                queue.append((ni, nj))

    return dp[-1][-1]

grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
print(min_path_sum(grid))
