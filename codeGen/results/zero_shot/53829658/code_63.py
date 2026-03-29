from collections import defaultdict, deque

def solve():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)

    capital_cities = []
    min_reversals = float('inf')

    # Perform DFS from each vertex to find the number of reversals
    for city in range(1, n+1):
        visited = set()
        queue = deque([(city, 0)])  # (city, reversals)
        while queue:
            city, reversals = queue.popleft()
            if city not in visited:
                visited.add(city)
                for neighbor in graph[city]:
                    if neighbor not in visited:
                        queue.append((neighbor, reversals + 1))
        capital_cities.append((reversals, city))

    # Find the minimum number of reversals and the corresponding capital cities
    min_reversals = min(cities[0] for cities in capital_cities)
    capital_cities = [city for city, _ in capital_cities if _ == min_reversals]

    print(min_reversals)
    print(*capital_cities, sep='\n')

solve()
