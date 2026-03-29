from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)

min_edges = float('inf')
capital_cities = []
for city in range(1, n+1):
    edges_to_capital = 0
    for adjacent_city in graph[city]:
        if dp[adjacent_city][0] < dp[city][0]:
            edges_to_capital += 1
    min_edges = min(min_edges, edges_to_capital)
    capital_cities.append(city)

print(min_edges)
print(' '.join(map(str, capital_cities)))
