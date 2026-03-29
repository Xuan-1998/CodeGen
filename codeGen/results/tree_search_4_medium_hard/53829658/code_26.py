import sys
from collections import deque

def find_minimum_reversed_edges_and_capitals():
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    # Initialize dp array with infinity values except dp[0] which is 0
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        queue = deque([(i, 0)])  # (city, reversed_edges)
        while queue:
            city, reversed_edges = queue.popleft()
            if dp[city] <= reversed_edges:
                continue
            dp[city] = reversed_edges
            for neighbor in graph[city]:
                queue.append((neighbor, reversed_edges + 1))

    min_reversed_edges = min(dp[1:])
    capitals = [i for i in range(1, n + 1) if dp[i] == min_reversed_edges]

    print(min_reversed_edges)
    print(' '.join(map(str, capitals)))

find_minimum_reversed_edges_and_capitals()
