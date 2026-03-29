import sys
from collections import deque

def solve():
    n = int(sys.stdin.readline())
    graph = [[] for _ in range(n+1)]
    dp = [float('inf')] * (n+1)
    parent = [-1] * (n+1)

    for _ in range(n-1):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([0])
    dp[0] = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dp[neighbor] > dp[node] + 1:
                dp[neighbor] = dp[node] + 1
                parent[neighbor] = node
                queue.append(neighbor)

    max_distance = max(dp[1:])
    paths = []

    for i in range(1, n+1):
        if dp[i] == max_distance:
            path = []
            while i != 0:
                path.append(i)
                i = parent[i]
            paths.append(list(reversed(path)))

    return str(max_distance) + '\n' + ' '.join(map(str, min(paths)))

print(solve())
