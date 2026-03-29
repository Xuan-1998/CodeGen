from collections import defaultdict

def infinite_zoo():
    q = int(input())
    graph = defaultdict(list)
    
    for _ in range(q):
        u, v = map(int, input().split())
        graph[u].append(v)
        
    visited = [[False] * 2**30 for _ in range(2**30)]
    
    def dfs(u):
        for v in graph[u]:
            if not visited[v][u & v]:
                visited[v][u & v] = True
                dfs(v)
                
    for u in range(2**30):
        if not visited[u][0]:
            dfs(u)
            
    while q:
        u, v = map(int, input().split())
        print('YES' if visited[v][u] else 'NO')
        q -= 1

infinite_zoo()
