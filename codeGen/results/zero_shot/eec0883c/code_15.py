from collections import deque

def find_max_gasoline():
    n = int(input())
    w = list(map(int, input().split()))
    graph = {}
    for _ in range(n - 1):
        u, v, c = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, c))
        graph[v].append((u, c))

    max_gasoline = 0
    visited = set()
    queue = deque([(1, w[0])])

    while queue:
        city, gasoline = queue.popleft()
        if city not in visited:
            visited.add(city)
            max_gasoline = max(max_gasoline, gasoline)

            for neighbor, length in graph.get(city, []):
                new_gasoline = min(gasoline, length)
                queue.append((neighbor, w[neighbor - 1] + new_gasoline))

    return max_gasoline

print(find_max_gasoline())
