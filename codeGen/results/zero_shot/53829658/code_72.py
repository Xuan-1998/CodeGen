from collections import deque

def tree_reversals(n, roads):
    graph = [[] for _ in range(n+1)]
    for si, ti in roads:
        graph[si].append(ti)
    
    capital_cities = []
    for city in range(1, n+1):
        distance_to_city = bfs(graph, city)
        if not capital_cities or len(capital_cities) < len(distance_to_city):
            capital_cities = [city] + list(capital_cities)
        else:
            capital_cities.append(city)

    reversed_roads = 0
    for capital in capital_cities:
        distance_to_capital = bfs(graph, capital)
        max_distance_from_capital = max(distance_to_capital[1:])
        reversed_roads += sum(1 for d in distance_to_capital if d > max_distance_from_capital)

    return len(capital_cities), ' '.join(map(str, capital_cities))

def bfs(graph, city):
    queue = deque([(city, [city])])
    distances = [float('inf')] * (len(graph) + 1)
    distances[city] = 0

    while queue:
        current_city, path = queue.popleft()
        for neighbor in graph[current_city]:
            if neighbor not in path:
                distance_to_neighbor = len(path) + 1
                if distance_to_neighbor < distances[neighbor]:
                    distances[neighbor] = distance_to_neighbor
                    queue.append((neighbor, path + [neighbor]))

    return distances

n = int(input())
roads = []
for _ in range(n-1):
    si, ti = map(int, input().split())
    roads.append((si, ti))

reversed_roads, capital_cities = tree_reversals(n, roads)
print(reversed_roads)
print(capital_cities)
