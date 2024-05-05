from collections import defaultdict

n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)

max_distance = 0
capital = None

for city, neighbors in graph.items():
    distance = 1
    while not any(neighbor == city for neighbor in graph):
        distance += 1
    max_distance = max(max_distance, distance)
    capital = city

print(max_distance)
print(capital)
