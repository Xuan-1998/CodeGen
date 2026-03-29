from collections import defaultdict

def treeland_problem():
    n = int(input())
    graph = defaultdict(list)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
    
    capital_in_degree = [0] * (n + 1)
    for city, neighbors in graph.items():
        for neighbor in neighbors:
            capital_in_degree[neighbor] += 1

    max_in_degree_city = max(range(1, n + 1), key=lambda x: capital_in_degree[x])

    # Actual reversal count
    reversed_road_count = [0] * (n + 1)
    visited = set()

    def dfs(city):
        if city in visited:
            return 0
        visited.add(city)

        for neighbor in graph[city]:
            reversed_road_count[neighbor] += 1
            dfs(neighbor)

    dfs(max_in_degree_city)

    print(sum(reversed_road_count))
    print(*reversed(range(n, 0, -1)), sep=' ')

treeland_problem()
