import sys
from collections import defaultdict

def solve():
    n = int(sys.stdin.readline())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)

    capital_cities = []
    min_edges = float('inf')
    for city in range(1, n+1):
        if len(graph[city]) == 0:
            continue
        edges = 0
        parent = {city: None}
        visited = set([city])
        stack = [city]
        while stack:
            node = stack.pop()
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    parent[neighbor] = node
                    edges += 1
        capital_cities.append(edges)
        min_edges = min(min_edges, edges)

    print(min_edges)
    print(*sorted((city for city, edges in zip(range(1, n+1), capital_cities) if edges == min_edges)), sep='\n')

if __name__ == '__main__':
    solve()
