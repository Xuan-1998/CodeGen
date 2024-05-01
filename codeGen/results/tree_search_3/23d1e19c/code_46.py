import sys

def solve():
    n, m = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)

    s, t, k = map(int, input().split())
    path = list(map(int, input().split()))
    recomputations = [0] * (n + 1)
    recomputations[s - 1] = sys.maxsize

    for i in range(1, n):
        if i == path[k - 1]:
            recomputations[i] = recomputations[i - 1]
            k -= 1
        else:
            recomputations[i] = min(recomputations[i - 1] + 1, recomputations[path[k - 1]] + 1)

    print(*recomputations[1:], sep=' ')
