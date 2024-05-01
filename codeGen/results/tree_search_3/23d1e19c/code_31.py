from collections import deque

def find_max_recomputation(n, m, edges, s, t):
    # Build graph and compute in-degree of each vertex
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for u, v in edges:
        graph[v].append(u)
        indegree[u] += 1

    # BFS to find the shortest path from s to t
    queue = deque([s])
    parent = [-1] * (n+1)
    while queue and queue[0] != t:
        u = queue.popleft()
        for v in graph[u]:
            if indegree[v] == 0:
                queue.append(v)
                parent[v] = u
                indegree[v] -= 1

    # Compute the recomputation needed at each vertex
    f = [float('inf')] * (n+1)
    f[t] = 0
    for i in range(n-1, -1, -1):
        if parent[i] != -1:
            min_recomputation = float('inf')
            max_recomputation = 0
            for j in range(i+1, t+1):
                if has_edge(j, i):
                    min_recomputation = min(min_recomputation, f[j])
                    max_recomputation = max(max_recomputation, f[j])
            f[i] = max_recomputation + (min_recomputation != float('inf'))
        else:
            f[i] = 0

    return f[s], f[t]
