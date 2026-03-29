import sys

def dfs(graph, node, visited, parent):
    count = 0
    for neighbor in graph[node]:
        if neighbor != parent:
            if neighbor not in visited:
                visited.add(neighbor)
                count += 1 + dfs(graph, neighbor, visited, node)
            else:
                count += 1
    return count

n = int(sys.stdin.readline())
graph = {}
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)

min_count = float('inf')
capital_cities = []

for city in range(1, n+1):
    visited = set()
    count = dfs(graph, city, visited, None)
    if count < min_count:
        min_count = count
        capital_cities = [city]
    elif count == min_count:
        capital_cities.append(city)

print(min_count)
print(*capital_cities, sep='\n')
