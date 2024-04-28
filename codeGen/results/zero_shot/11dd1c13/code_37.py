import sys
from collections import deque

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def solve():
    queue = deque([(0, 0, float('inf'))]) 
    visited = {(0, 0)}
    
    while queue:
        x, y, total = queue.popleft()
        
        if x == n - 1:
            return total
        
        for dx, dy in [(0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            
            if (nx, ny) not in visited:
                if grid[nx][ny] != 0:
                    queue.append((nx, ny, total - grid[nx][ny]))
                    visited.add((nx, ny))
                else:
                    queue.append((nx, ny, total))
                    visited.add((nx, ny))

print(solve())
