import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node, parent, path):
    global max_path_len
    global visited

    if len(path) > max_path_len:
        max_path_len = len(path)

    visited[node] = True
    for neighbor in graph[node]:
        if neighbor != parent and not visited[neighbor]:
            dfs(neighbor, node, path + [node])
    visited[node] = False

max_path_len = 0
visited = [False] * (n+1)

for i in range(1, n+1):
    if not visited[i]:
        dfs(i, -1, [])

def count_spines():
    global max_path_len

    spine_count = 0
    for i in range(m):
        u, v = graph[i]
        if len(path[u:v+1]) > 0 and (u not in path[u:v+1] or v not in path[u:v+1]):
            spine_count += 1

    return max_path_len * spine_count

path = [0] * (n+1)
print(count_spines())
