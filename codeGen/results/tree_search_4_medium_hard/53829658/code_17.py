from collections import defaultdict

def treeland(n, roads):
    graph = defaultdict(list)
    for si, ti in roads:
        graph[si].append(ti)

    # Calculate the shortest distance from each city to the capital
    dist = [float('inf')] * (n + 1)
    dist[0] = 0

    stack = [(i, 0) for i in range(1, n + 1)]
    while stack:
        city, parent_dist = stack.pop()
        for neighbor in graph[city]:
            if dist[neighbor] > dist[city] + 1:
                dist[neighbor] = dist[city] + 1
                stack.append((neighbor, dist[neighbor]))

    # Determine which cities are reachable with 0 or more reversed edges
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if dist[j] <= dist[i]:
                dp[i][j] = True

    # Find the optimal capital choices
    capitals = set(range(1, n + 1))
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if not dp[i][j]:
                capitals -= {i, j}

    min_reversed_edges = len(capitals)
    capital_choices = sorted(list(capitals))

    print(min_reversed_edges)
    print(*capital_choices)

n = int(input())
roads = [list(map(int, input().split())) for _ in range(n - 1)]
treeland(n, roads)
