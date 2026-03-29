n = int(input())
w = list(map(int, input().split()))
roads = []
for _ in range(n-1):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

graph = {}
for u, v, c in roads:
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, c))
    graph[v].append((u, c))

def max_gasoline(city):
    if w[city-1] == 0:
        return 0
    max_g = w[city-1]
    for neighbor, c in graph.get(city, []):
        remaining_c = c - (w[city-1] // (c + 1))
        if remaining_c > 0 and w[neighbor-1] > 0:
            new_max_g = min(max_gasoline(neighbor), max_g)
            if new_max_g < max_g:
                max_g = new_max_g
    return max_g

print(max(map(max_gasoline, range(1, n+1))))
