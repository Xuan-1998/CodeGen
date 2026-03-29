from collections import defaultdict

def min_inverse_roads(n, roads):
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)

    memo = {0: 0}

    def dfs(city):
        if city not in memo:
            children = [v for v in graph[city]]
            memo[city] = 1 + min(dfs(child) for child in children)
        return memo[city]

    capital_city = min((city for city in range(1, n+1)), key=dfs)

    inverse_roads = sum(dfs(city) for city in range(1, n+1)) - dfs(capital_city)
    capital_cities = [city for city in range(1, n+1) if dfs(city) == dfs(capital_city)]

    print(inverse_roads)
    print(' '.join(map(str, capital_cities)))

n = int(input())
roads = [list(map(int, input().split())) for _ in range(n-1)]
min_inverse_roads(n, roads)
