import sys

def read_input():
    n = int(input())
    graph = {}
    for _ in range(n - 1):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
    return n, graph

def dfs(graph, city, visited, dp, distance):
    visited.add(city)
    dp[city] = min(dp.get(city, float('inf')), distance)
    for neighbor in graph[city]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, dp, distance + 1)

n, graph = read_input()
dp = {i: float('inf') for i in range(1, n + 1)}
max_distance = 0
for city in range(1, n + 1):
    if city not in dp:
        visited = set()
        dfs(graph, city, visited, dp, 0)
        max_distance = max(max_distance, dp[city])
print(max_distance)

capital_cities = []
max_distance = 0
for city in range(1, n + 1):
    if city not in dp or dp[city] > max_distance:
        capital_cities.append(city)
        max_distance = dp[city]
print(*capital_cities, sep='\n')
