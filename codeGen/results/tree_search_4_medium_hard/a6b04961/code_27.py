from collections import defaultdict
import sys

def find_max_beauty():
    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dp = [0] * (n + 1)
    visited = set()

    for i in range(2, n + 1):
        dp[i] = max(dp[i-1], 1) if i not in visited else 0
        for j in list(graph):
            if i - 1 in graph[j]:
                graph[j].remove(i - 1)
                visited.add(i - 1)

    return max(dp)

print(find_max_beauty())
