import sys
from collections import defaultdict

n = int(input())
gasoline_capacities = list(map(int, input().split()))
roads = []
for _ in range(n - 1):
    roads.append(list(map(int, input().split())))

graph = defaultdict(list)
for road in roads:
    u, v, c = road
    graph[u].append((v, c))
    graph[v].append((u, c))

def dfs(node, remaining_gasoline):
    if node == n - 1:  # we have reached the destination city
        return remaining_gasoline

    max_gasoline = 0
    for neighbor, capacity in graph[node]:
        if remaining_gasoline >= capacity:
            gasolina_left = min(remaining_gasoline, gasoline_capacities[neighbor])
            max_gasoline = max(max_gasoline, dfs(neighbor, gasolina_left - capacity) + gasolina_left)
    return max_gasoline

print(dfs(0, gasoline_capacities[0]))
