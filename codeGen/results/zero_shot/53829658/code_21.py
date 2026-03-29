import sys

n = int(sys.stdin.readline())
graph = {}
for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u] = graph.get(u, []) + [v]
    graph[v] = graph.get(v, []) + [u]

capital = next(iter(graph))
reversed_edges = 0
for city, neighbors in graph.items():
    if city != capital:
        reversed_edges += len(neighbors) - 1

print(reversed_edges)
print(*sorted(graph.keys()), sep='\n')
