def dfs(v, visited):
    if v == -1:  # reached the end of the tail
        return 0
    if visited[v]:
        return 0
    visited[v] = True
    spine_count = 0
    for w in graph[v]:
        if not visited[w]:
            spine_count += dfs(w, visited)
    return spine_count + 1

max_beaauty = 0

for u in range(1, n+1):
    visited = [False] * (n+1)
    tail_len = dfs(u, visited)
    max_beaauty = max(max_beaauty, tail_len * len([w for w in graph[u] if not visited[w]]))

print(max_beaauty)
