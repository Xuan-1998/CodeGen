import sys

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    edges = []
    for _ in range(n-1):
        u, v = map(int, input().split())
        edges.append((u-1, v-1))

    xor_values = [0] * (n+1)
    visited = [False] * n

    def dfs(node):
        visited[node] = True
        for neighbor in edges:
            if neighbor[0] == node and not visited[neighbor[1]]:
                dfs(neighbor[1])
            elif neighbor[1] == node and not visited[neighbor[0]]:
                dfs(neighbor[0])
        xor_values[node] = values[node]
        for neighbor in edges:
            if neighbor[0] == node and not visited[neighbor[1]]:
                xor_values[node] ^= xor_values[neighbor[1]]
            elif neighbor[1] == node and not visited[neighbor[0]]:
                xor_values[node] ^= xor_values[neighbor[0]]

    for i in range(n):
        if not visited[i]:
            dfs(i)

    for i in range(1, n+1):
        if xor_values[i] != 0:
            return "NO"
    return "YES"

print(solve())
