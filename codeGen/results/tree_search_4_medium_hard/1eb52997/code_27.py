from collections import deque

def count_mirrors(N):
    grid = [list(input().strip()) for _ in range(N)]
    
    dp = [[0] * N for _ in range(N)]
    queue = deque([(0, 0)])
    
    while queue:
        i, j = queue.popleft()
        
        if i == N - 1 or grid[i][j + 1] == '#':
            continue
        
        visible_rocks = False
        for k in range(j + 1, N):
            if grid[i][k] == '#':
                visible_rocks = True
                break
        
        if not visible_rocks:
            dp[i][j] = 1
            queue.extend([(i, k) for k in range(j + 1, N)])
    
    return sum(sum(row) for row in dp)

T = int(input())
for _ in range(T):
    N = int(input())
    print(count_mirrors(N))
