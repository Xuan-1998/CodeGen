from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
s, t, k = map(int, input().split())
path = list(map(int, input().split()))


def dfs(v, path):
    visited.add(v)
    for next_v in graph[v]:
        if next_v == t:
            return True
        if not visited[next_v] and dfs(next_v, path + [next_v]):
            return True
    return False

visited = set()
min_recomputation = 0
max_recomputation = float('inf')

for i in range(k):
    v = path[i]
    if v == s or v == t:
        continue
    min_recomputation = min(min_recomputation, dfs(v, path[:i + 1]))
    max_recomputation = min(max_recomputation, len(path) - i - 1)

print(min_recomputation, max_recomputation)
