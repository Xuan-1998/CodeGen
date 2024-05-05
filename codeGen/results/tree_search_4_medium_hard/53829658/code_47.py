import sys
from collections import defaultdict

def solve():
    n = int(input())
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)

    capital = 1
    visited = [False] * (n+1)
    distance = [float('inf')] * (n+1)

    def dfs(u, parent):
        nonlocal capital
        if not visited[u]:
            visited[u] = True
            for v in graph[u]:
                if v != parent:
                    dfs(v, u)
                    if distance[v] < float('inf'):
                        distance[u] = min(distance[u], 1 + distance[v])

    dfs(capital, -1)

    print(min(distance[1:] or [0]))
    print(*sorted(i for i in range(2, n+1) if distance[i] == min(distance[1:]) or [1]), sep='\n')

if __name__ == "__main__":
    solve()
