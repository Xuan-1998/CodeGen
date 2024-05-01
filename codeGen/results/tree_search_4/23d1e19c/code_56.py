import sys
from collections import deque

def shortest_path_recomputation(graph, s, t):
    n = len(graph)
    min_count = [float('inf')] * (n + 1)
    max_count = [0] * (n + 1)

    def dfs(v):
        if v == t:
            return 0, 0

        if min_count[v] != float('inf'):
            return min_count[v], max_count[v]

        min_recomputation, max_recomputation = float('inf'), 0
        for u in graph.get(v, []):
            rec_min, rec_max = dfs(u)
            if not rec_min:
                rec_min = rec_max + 1

            if not rec_max:
                rec_max = rec_min + 1

            min_recomputation = min(min_recomputation, rec_min + 1)
            max_recomputation = max(max_recomputation, rec_max + 1)

        min_count[v] = min_recomputation
        max_count[v] = max_recomputation

        return min_recomputation - 1, max_recomputation - 1 if s != v else (min_recomputation - 1, max_recomputation - 1)

    return dfs(s)[0], dfs(s)[1]

n, m = map(int, input().split())
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)  # Assuming the graph is undirected

k = int(input())
path = list(map(int, input().split()))
print(*shortest_path_recomputation(graph, path[0], path[-1]))
