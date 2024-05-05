import sys
from collections import deque

def solve():
    n = int(sys.stdin.readline())
    w = list(map(int, sys.stdin.readsplitlines(1)[0].split()))
    graph = {}
    for i in range(n-1):
        u, v, c = map(int, sys.stdin.readline().split())
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, c))
        graph[v].append((u, c))

    def dfs(node, gas):
        visited.add(node)
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, min(gas, cost))
        return gas

    max_gas = 0
    visited = set()
    for i in range(n):
        gas = w[i]
        while graph[i]:
            node, cost = graph[i].pop(0)
            gas = dfs(node, gas)
        max_gas = max(max_gas, gas)

    print(max_gas)

if __name__ == "__main__":
    solve()
