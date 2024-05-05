import sys

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]

for i in range(1, n):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)

def dfs(graph, node, visited, reverse_count):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, reverse_count + 1)
    return reverse_count

capital_cities = []

for i in range(1, n+1):
    visited = [False] * (n+1)
    reverse_count = dfs(graph, i, visited, 0)
    capital_cities.append((i, reverse_count))

min_reverse_count = min(count for _, count in capital_cities)

optimal_capitals = [capital for capital, _ in capital_cities if _ == min_reverse_count]

print(min_reverse_count)
for capital in optimal_capitals:
    print(capital, end=' ')
print()
