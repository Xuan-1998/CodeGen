from collections import deque

def solve():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # Perform BFS from each node to find the shortest distance
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    for _ in range(n):
        queue = deque([i for i, d in enumerate(dist) if d == _])
        while queue:
            curr_node = queue.popleft()
            for neighbor in graph[curr_node]:
                dist[neighbor] = min(dist[neighbor], dist[curr_node] + 1)
    capital_city_idx = dist.index(min(dist))
    min_reversals = sum(1 for x, y in enumerate(graph) if x != capital_city_idx and any(x == z for z in y))

    # Print the minimum number of roads to be reversed
    print(min_reversals)

    # Find all possible ways to choose the capital
    capital_cities = [i for i, d in enumerate(dist) if d == min(dist)]
    print(' '.join(map(str, capital_cities)))

solve()
