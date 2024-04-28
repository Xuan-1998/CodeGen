from collections import deque

def num_paths_to_collect_k_coins(k, n, arr):
    queue = deque([(0, 0, 0)])
    visited = set((0, 0))
    res = 0
    
    while queue:
        i, j, cnt = queue.popleft()
        
        if cnt > k:
            continue
        
        if i == n-1 and j == n-1 and cnt == k:
            return 1
        
        for dx, dy in [(1, 0), (0, 1)]:
            x, y = i+dx, j+dy
            
            if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                if arr[x][y] > 0:
                    queue.append((x, y, cnt + arr[x][y]))
                    visited.add((x, y))
                else:
                    queue.append((x, y, cnt))
                    visited.add((x, y))
                    
    return res
