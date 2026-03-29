from collections import defaultdict, deque

n = int(input())
roads = []
for _ in range(n-1):
    si, ti = map(int, input().split())
    roads.append((si-1, ti-1)) # subtract 1 because indices are 0-based

graph = defaultdict(list)
for road in roads:
    graph[road[0]].append(road[1])

def bfs(graph, start):
    queue = deque([(start, 0)]) # (node, distance)
    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0
    while queue:
        node, dist = queue.popleft()
        for neighbor in graph[node]:
            if dist + 1 < distances[neighbor]:
                distances[neighbor] = dist + 1
                queue.append((neighbor, dist + 1))
    return max(distances.values())

capital = bfs(graph, 0) # start from city 0

min_edges = n - 1 - capital
print(min_edges)

capital_cities = [i+1 for i in range(n)]
for city in sorted(capital_cities):
    print(city)
