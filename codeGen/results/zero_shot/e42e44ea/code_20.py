import sys
from collections import deque

def min_points_required(N, M, grid):
    dp = [[float('inf')] * N for _ in range(M)]
    dp[0][0] = 0
    
    directions = [(0, 1), (1, 0)]  # right, down
    
    queue = deque([(0, 0)])
    
    while queue:
        x, y = queue.popleft()
        
        if x == M - 1 and y == N - 1:
            return dp[M-1][N-1]
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if (0 <= nx < M) and (0 <= ny < N) and grid[nx][ny] > 0:
                new_points = max(0, dp[x][y] - grid[nx][ny])
                
                if new_points < dp[nx][ny]:
                    queue.append((nx, ny))
                    dp[nx][ny] = new_points
    
    return -1

# Test cases
N, M = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(N)]

print(min_points_required(N, M, grid))

