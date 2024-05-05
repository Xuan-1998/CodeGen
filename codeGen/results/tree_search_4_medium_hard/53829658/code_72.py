import sys
from collections import defaultdict, deque

def solution():
    n = int(sys.stdin.readline())
    graph = defaultdict(int)
    in_degree = [0] * (n + 1)

    # Read the graph and calculate in-degrees of each city
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u] += 1
        graph[v] -= 1
        in_degree[u] += 1
        in_degree[v] -= 1

    # Find the maximum in-degree (capital city)
    capital_city = max(range(1, n + 1), key=lambda x: abs(in_degree[x]))

    # Initialize dp[][] and queue
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    queue = deque([(capital_city, 0)])

    # Perform BFS to fill dp[][] with reachability information
    while queue:
        city, k = queue.popleft()
        if not dp[city][k]:
            dp[city][k] = True
            for neighbor in range(1, n + 1):
                if graph[neighbor] > 0 and (not dp[neighbor][k - 1] or city != capital_city):
                    queue.append((neighbor, k + 1))

    # Find the minimum number of reversed roads to reach any other city
    min_reversed_roads = max(k for k in range(n) if dp[n][k])

    # Print the minimum number of reversed roads and all possible ways to choose the capital
    print(min_reversed_roads)
    for city in range(1, n + 1):
        if dp[city][min_reversed_roads]:
            print(city, end=' ')
    print()

solution()
