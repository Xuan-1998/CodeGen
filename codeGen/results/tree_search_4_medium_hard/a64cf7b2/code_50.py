===BEGIN CODE===
from collections import defaultdict
def max_vertices(n, m, T):
    graph = defaultdict(list)
    for _ in range(m):
        u, v, t = map(int, input().split())
        graph[u].append((v, t))
    
    dp = [[0] * (T + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)
    visited[1] = True
    
    def dfs(i, j):
        if visited[i]:
            return 0
        visited[i] = True
        max_visited = 1
        for v, t in graph[i]:
            if j >= t:
                visited[v] = True
                max_visited += dfs(v, j - t)
        return max_visited
    
    ans = dfs(1, T)
    path = []
    i, j = n, T
    while i > 1 and j > 0:
        for v, t in graph[i]:
            if j >= t and visited[v]:
                path.append(i)
                j -= t
                i = v
                break
        else:
            i -= 1
            j -= 1
    
    return ans, ' '.join(map(str, reversed(path)))

n, m, T = map(int, input().split())
ans, path = max_vertices(n, m, T)
print(ans)
print(path)
===END CODE===
