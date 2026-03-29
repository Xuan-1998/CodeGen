from collections import defaultdict, deque

def solve():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
    capital_cities = []
    visited = set()
    for i in range(1, n+1):
        if i not in visited:
            queue = deque([i])
            visited.add(i)
            while queue:
                city = queue.popleft()
                for neighbor in graph[city]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            capital_cities.append((min(visited), i))
    capital_cities.sort(key=lambda x: x[0])
    min_inverse_edges = float('inf')
    for capital, city in capital_cities:
        inverse_edges = 0
        for neighbor in graph[city]:
            if neighbor not in visited:
                inverse_edges += 1
        if inverse_edges < min_inverse_edges:
            min_inverse_edges = inverse_edges
    print(min_inverse_edges)
    print(*capital_cities, sep='\n')
