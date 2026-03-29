import sys

def solve():
    n = int(sys.stdin.readline())
    graph = {}
    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        if u not in graph: graph[u] = []
        if v not in graph: graph[v] = []
        graph[u].append(v)
        graph[v].append(u)

    max_distance = [0] * (n + 1)
    visited = [False] * (n + 1)
    stack = [(1, 0)]  # (node, distance)

    while stack:
        node, dist = stack.pop()
        if not visited[node]:
            visited[node] = True
            max_distance[node] = dist
            for neighbor in graph.get(node, []):
                if not visited[neighbor]:
                    stack.append((neighbor, dist + 1))

    min_inversions = max(max_distance[1:])
    capitals = [i for i, d in enumerate(max_distance) if d == min_inversions]

    print(min_inversions)
    print(" ".join(map(str, capitals)))

solve()
