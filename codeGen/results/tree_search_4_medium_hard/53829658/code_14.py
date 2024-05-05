from collections import defaultdict
import sys

def solve():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)

    capital = 1
    reachable = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(i - 1, -1, -1):
            if graph[j]:
                reachable[i][j] = True
            else:
                break

    min_reversed_edges = float('inf')
    capitals = []
    for i in range(2, n + 1):
        if all(reachable[j][i] for j in range(i)):
            if sum(int(reachable[j][i]) for j in range(i)) < min_reversed_edges:
                min_reversed_edges = sum(int(reachable[j][i]) for j in range(i))
                capitals = list(range(1, i))

    print(min_reversed_edges)
    print(*capitals, sep=' ')

solve()
