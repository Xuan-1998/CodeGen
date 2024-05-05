import sys
from collections import deque

def solve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        grid = [list(sys.stdin.readline().strip()) for _ in range(N)]
        
        count = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '.':
                    queue = deque([(i, j)])
                    visited = {(i, j)}
                    while queue:
                        x, y = queue.popleft()
                        if (x + 1 < N) and ((x + 1, y) not in visited) and (grid[x + 1][y] == '.'):
                            queue.append((x + 1, y))
                            visited.add((x + 1, y))
                        if (y + 1 < N) and ((x, y + 1) not in visited) and (grid[x][y + 1] == '.'):
                            queue.append((x, y + 1))
                            visited.add((x, y + 1))
                    count += len(visited)
        
        print(count)

if __name__ == "__main__":
    solve()
