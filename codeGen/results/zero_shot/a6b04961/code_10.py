import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)  # Assuming the graph is undirected

visited = [False] * (n+1)
max_tail_length = 0
spine_count = 0

def dfs(v, parent, path_len):
    global max_tail_length
    visited[v] = True
    path_len += 1

    if all(visited[u] for u in graph[v]):
        max_tail_length = path_len

    for neighbor in graph[v]:
        if neighbor != parent:
            dfs(neighbor, v, path_len)

    visited[v] = False

def find_spines():
    global spine_count

    for edge in graph:
        u, v = edge
        if visited[u] or visited[v]:
            continue
        spine_count += 1

# Perform DFS to detect simple paths (tails)
for i in range(1, n+1):
    dfs(i, -1, 0)

# Find spines
find_spines()

# Calculate the beauty
beauty = max_tail_length * spine_count

print(beauty)
