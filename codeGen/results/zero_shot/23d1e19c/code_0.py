from collections import deque
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
p = list(map(int, input().split()))
min_recompute = float('inf')
max_recompute = -float('inf')

def bfs(u, t):
    dist = [-1] * (n + 1)
    q = deque([u])
    dist[u] = 0
    while q:
        v = q.popleft()
        if v == t:
            return dist[v]
        for w in graph[v]:
            if dist[w] == -1:
                q.append(w)
                dist[w] = dist[v] + 1
    return -1

for i in range(len(p) - 1):
    min_recompute = min(min_recompute, bfs(p[i], p[i + 1]))
print(f"{min_recompute} {max_recompute}")
