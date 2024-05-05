import sys

def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def solve():
    n = int(sys.stdin.readline())
    graph = {}
    for i in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)
    
    visited = set()
    root = None
    for node in graph:
        if node not in visited:
            dfs(graph, node, visited)
            root = node
            break
    
    min_distance = 0
    distances = {node: 0 for node in graph}
    queue = [(root, 1)]
    while queue:
        node, distance = queue.pop(0)
        if distance > min_distance:
            min_distance = distance
        for neighbor in graph[node]:
            if neighbor not in distances or distances[neighbor] < distance+1:
                distances[neighbor] = distance+1
                queue.append((neighbor, distance+1))
    
    print(min_distance-1)  # subtract 1 because we're counting from the root
    
    capital_cities = []
    for node in graph:
        if distances[node] == min_distance:
            capital_cities.append(node)
    capital_cities.sort()
    for city in capital_cities:
        print(city, end=' ')
    print()

if __name__ == "__main__":
    solve()
