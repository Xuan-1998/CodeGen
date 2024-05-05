import heapq
from collections import defaultdict

def hedgehog_beauty(n, m, edges):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        in_degree[v] += 1
        in_degree[u] += 1

    pq = [(in_degree[i], i) for i in range(1, n + 1)]
    heapq.heapify(pq)

    memo = [[0, set(), 0] for _ in range(n + 1)]

    while pq:
        degree, vertex = heapq.heappop(pq)
        if not memo[vertex][0]:
            for neighbor in graph[vertex]:
                old_degree = degree
                degree -= 1
                if degree > 0:
                    heapq.heappush(pq, (degree, neighbor))
                else:
                    neighbors = set(graph[neighbor])
                    visited_neighbors = len(neighbors) - 1

                    memo[neighbor][0] = max(memo[neighbor][0], memo[vertex][0] + (visited_neighbors + 1))
                    memo[neighbor][2] += 1
        if degree == 0:
            return memo[vertex][0] * memo[vertex][2]

    return 0

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

print(hedgehog_beauty(n, m, edges))
