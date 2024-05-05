from functools import lru_cache

n, *w = map(int, input().split())
graph = {}
for i in range(n - 1):
    u, v, c = map(int, input().split())
    graph[u] = graph.get(u, []) + [(v, c)]
    graph[v] = graph.get(v, []) + [(u, c)]

@lru_cache(None)
def dfs(i, j):
    if i == 0:
        return w[0]
    res = 0
    for v, c in graph[i]:
        res = max(res, dfs(v, min(j - c, w[v])) or dfs(v, j))
    return res

print(dfs(n - 1, w[-1]))
