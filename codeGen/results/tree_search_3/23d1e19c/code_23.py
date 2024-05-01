import sys

def min_max_recomputations():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    s, t = map(int, input().split())
    k = int(input())

    # Preprocess the graph to find all shortest paths
    f = [0] * (n+1)
    for i in range(1, n+1):
        if i != t:
            f[i] = max(f[v] for v in range(i+1, t+1)) + 1

    # Find the minimum and maximum number of recomputations
    min_recomputations = 0
    max_recomputations = 0
    for i in range(1, k):
        if graph[p[i-1]][i] != p[i]:
            min_recomputations += 1
            max_recomputations = max(max_recomputations, f[graph[p[i-1]][i]] + (f[t] if t > i else 0))

    print(min_recomputations, max_recomputations)

min_max_recomputations()
