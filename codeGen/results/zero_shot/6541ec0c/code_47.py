import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u-1, v-1))

    # Perform DFS to identify connected components
    component_values = {}
    visited = [False] * n

    def dfs(node):
        if not visited[node]:
            visited[node] = True
            value = values[node]
            for neighbor in graph[node]:
                value ^= dfs(neighbor)
            return value
        return 0

    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    for node in range(n):
        if not visited[node]:
            component_values[dfs(node)] = None

    # Check if all connected components have the same bitwise XOR value
    xor_values = list(component_values.keys())
    if len(xor_values) > 1:
        print("NO")
    else:
        print("YES" if len(xor_values) == 0 or len(xor_values) == 1 and xor_values[0] == 0 else "NO")

solve()
