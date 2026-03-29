n = int(input())
edges = []
for _ in range(n-1):
    si, ti = map(int, input().split())
    edges.append((si, ti))
graph = {i: [] for i in range(1, n+1)}
for si, ti in edges:
    graph[si].append(ti)
capital = min(graph, key=lambda x: len([y for y in graph if y in graph[x]]))
min_reversed_edges = sum(len([y for y in graph if y not in graph[city]]) for city in range(1, n+1))
print(min_reversed_edges)
print(*sorted(range(1, n+1)), sep=' ')
