import sys

n, m = map(int, sys.stdin.readline().split())
graph = {}
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

def dfs(vertex, visited, path):
    if len(path) > 0:
        return len(path)
    visited.add(vertex)
    longest_path = 0
    for neighbor in graph.get(vertex, []):
        if neighbor not in visited:
            longest_path = max(longest_path, dfs(neighbor, visited, path + [vertex]))
    visited.remove(vertex)
    return longest_path

longest_tail = 0
for vertex in range(1, n+1):
    visited = set()
    longest_tail = max(longest_tail, dfs(vertex, visited, []))

spines = 0
visited = set()
for i in range(m):
    u, v = graph[i][0], graph[i][1]
    if (u in visited and v not in visited) or (u not in visited and v in visited):
        spines += 1

print(longest_tail * spines)
