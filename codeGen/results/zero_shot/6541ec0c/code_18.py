import sys
from collections import defaultdict

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    graph = defaultdict(list)

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = set()
    xor_values = {}

    def dfs(node):
        visited.add(node)
        xor_value = values[node]
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
                xor_value ^= values[neighbor]
        return xor_value

    for node in range(n):
        if node not in visited:
            xor_values[dfs(node)] = 1

    if len(xor_values) > 1 or (k - 1 >= len(xor_values) and len(xor_values)):
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    solve()
