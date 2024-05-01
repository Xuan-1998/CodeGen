import sys
from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
directions = [(1, 0), (1, 1), (1, -1)]  # down, right, left

for i in range(n):
    for j in range(n):
        if i == 0:  # base case: top row
            dp[i][j] = grid[i][j]
        else:
            queue = deque([(i, j)])
            visited = set((i, j))
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and (nx, ny) not in visited:
                        dp[i][j] = min(dp[i][j], dp[nx][ny-1] + grid[i][y])
                        queue.append((nx, ny))
                        visited.add((nx, ny))

print(min(dp[-1]))
