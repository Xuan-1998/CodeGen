import sys

def dp_top_down(n, m, T):
    memo = {}

    def dfs(i, t):
        if (i, t) in memo:
            return memo[(i, t)]
        
        if i == 1: 
            return 0
        
        res = 0
        for edge in edges[i-1]:
            u, v, w = edge
            if t >= w and v not in visited:
                visited.add(v)
                res = max(res, dfs(v, t-w) + 1)
        
        memo[(i, t)] = res
        return res
    
    edges = [[] for _ in range(n+1)]
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges[u].append((u, v, w))
    
    visited = set()
    T -= 1  # subtract 1 because we need to traverse the edge from vertex n to itself
    
    res = dfs(n, T)
    return str(res)

n, m, T = map(int, sys.stdin.readline().split())
print(dp_top_down(n, m, T))
