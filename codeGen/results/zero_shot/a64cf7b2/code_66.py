import sys
from collections import defaultdict

n, m, T = map(int, input().split())
graph = defaultdict(list)
time_spent = [0] * (n + 1)

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

def dfs(u, time_limit):
    visited = set()
    max_visited = 0
    for v, t in graph[u]:
        if time_spent[v] + t <= time_limit:
            if v not in visited:
                visited.add(v)
                new_time_spent = time_spent[v] + t
                if new_time_spent > T:
                    break
                max_visited = max(max_visited, 1 + dfs(v, new_time_limit))
    return max_visited

max_visited = dfs(1, T)

print(max_visited)

# Print the visited vertices (this part is not required for the problem statement)
visited_vertices = []
for u in range(n + 1):
    if time_spent[u] > 0:
        visited_vertices.append(u)
print(*visited_vertices, sep='\n')
