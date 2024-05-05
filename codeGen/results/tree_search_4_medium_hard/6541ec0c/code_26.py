def can_delete_edges(n, k, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def dfs(node, parent, xor_min, xor_max):
        if xor_min == xor_max:
            return [xor_min]
        res = []
        for neighbor in graph[node]:
            if neighbor != parent:
                xor_neighbor = dfs(neighbor, node, min(xor_min, neighbor), max(xor_max, neighbor))
                if xor_neighbor:
                    res.append([min(xor_min, xor_neighbor[0]), max(xor_max, xor_neighbor[-1])])
        return [xor_min] + (res or [[xor_min], [xor_max]]) if not res else [xor_min] + res

    components = dfs(0, -1, 0, 0)
    return "YES" if len(components) <= k else "NO"

import sys
input = lambda: [int(x) for x in input().split()]
t = int(input())
for _ in range(t):
    n, k = input()
    edges = [list(map(int, input().split())) for _ in range(n-1)]
    print("YES" if can_delete_edges(n, k, edges) else "NO")
