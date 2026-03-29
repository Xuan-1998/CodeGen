from collections import defaultdict

def dfs(graph, memo, t, i):
    if (t, i) in memo:
        return memo[(t, i)]
    
    if t <= 0:
        return 0
    
    max_vertices = 0
    for edge in graph[i]:
        u, _ = edge
        t_edge, _ = edge[2]
        next_t = t - t_edge
        next_i = u
        vertices = dfs(graph, memo, next_t, next_i) + 1
        max_vertices = max(max_vertices, vertices)
    
    memo[(t, i)] = max_vertices
    return max_vertices

def solve():
    n, m, T = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
    
    memo = {}
    max_vertices = dfs(graph, memo, T, 1)
    path = []
    t, i = T, n
    while t > 0:
        path.append(i)
        for edge in graph[i]:
            u, _ = edge
            t_edge, _ = edge[2]
            if t >= t_edge:
                t -= t_edge
                i = u
                break
    
    print(max_vertices)
    print(*path[::-1])

solve()
