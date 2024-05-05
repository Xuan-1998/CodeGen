from collections import deque

def minInitialPoints(grid):
    N, M = len(grid), len(grid[0])
    
    dp = [[float('inf')] * M for _ in range(N)]
    visited = set((0, 0))

    queue = deque([(0, 0, grid[0][0])])

    while queue:
        i, j, points = queue.popleft()
        
        if i == N - 1 and j == M - 1: 
            return points

        for di, dj in [(0, 1), (1, 0)]:
            ni, nj = i + di, j + dj
            
            if 0 <= ni < N and 0 <= nj < M and (ni, nj) not in visited:
                visited.add((ni, nj))
                queue.append((ni, nj, points + grid[ni][nj]))
                
    return -1
