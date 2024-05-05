from collections import defaultdict

n = int(input())
graph = defaultdict(int)
for _ in range(n-1):
    si, ti = map(int, input().split())
    graph[si] += 1
    graph[ti] -= 1

capital = min(graph, key=graph.get)

reversed_edges = sum(1 for out_degree in graph.values() if out_degree < 0)
print(reversed_edges)

capital_cities = sorted(key for key, value in graph.items() if value == 0)
print(*capital_cities, sep='\n')
