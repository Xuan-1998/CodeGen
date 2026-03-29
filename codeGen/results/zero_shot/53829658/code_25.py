graph = {}
for _ in range(int(input())):
    si, ti = map(int, input().split())
    if si not in graph:
        graph[si] = []
    if ti not in graph:
        graph[ti] = []
    graph[si].append(ti)

capital = max(graph, key=lambda city: dfs(city, set(), 0))

def dfs(city, visited, distance):
    if city in visited:
        return distance
    visited.add(city)
    max_distance = 0
    for neighbor in graph[city]:
        if neighbor not in visited:
            max_distance = max(max_distance, dfs(neighbor, visited, distance + 1))
    visited.remove(city)
    return max_distance

print(min_edges_to_reverse(capital))

def min_edges_to_reverse(capital):
    visited = set()
    queue = [(capital, 0)]
    edges_to_reverse = 0
    while queue:
        city, distance = queue.pop(0)
        if city not in visited:
            visited.add(city)
            for neighbor in graph[city]:
                if neighbor != capital and neighbor not in visited:
                    queue.append((neighbor, distance + 1))
                    edges_to_reverse += distance
    return edges_to_reverse

def all_capitals():
    visited = set()
    queue = [(0, [0])]
    capitals = []
    while queue:
        _, path = queue.pop(0)
        if len(path) > 1 and path[-2] not in visited:
            continue
        visited.update(path)
        capitals.append(path[:-1])
        for neighbor in graph[path[-1]]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return capitals

print(*all_capitals(), sep='\n')
