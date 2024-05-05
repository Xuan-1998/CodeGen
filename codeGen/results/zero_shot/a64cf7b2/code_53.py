import sys
from collections import deque

def solve():
    n, m, T = map(int, input().split())
    graph = {}
    for _ in range(m):
        u, v, t = map(int, input().split())
        if u not in graph:
            graph[u] = []
        graph[u].append((v, t))

    dp = [0] * (n + 1)
    visited = set()
    queue = deque([(1, T)])

    while queue:
        node, time_left = queue.popleft()
        if node > n or time_left < 0:
            continue
        if node not in visited:
            visited.add(node)
            for neighbor, t in graph.get(node, []):
                new_time_left = time_left - t
                if new_time_left >= 0 and dp[neighbor] < dp[node] + 1:
                    dp[neighbor] = dp[node] + 1
                    queue.append((neighbor, new_time_left))

    k = max(dp)
    visited = set()
    result = []
    for i in range(2, n + 1):
        if dp[i] == k and i not in visited:
            visited.add(i)
            result.append(str(i))

    print(k)
    print(' '.join(result))

solve()
