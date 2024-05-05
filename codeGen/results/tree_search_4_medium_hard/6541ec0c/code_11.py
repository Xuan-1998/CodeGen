from collections import defaultdict
from functools import lru_cache

def solve():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    @lru_cache(None)
    def dfs(node, parent):
        if node not in values:
            return 0
        value = values[node]
        children = set(graph[node])
        children.discard(parent)
        for child in children:
            xor_value = dfs(child, node)
            if xor_value != value:
                return -1
        return value

    total_xor = 0
    for i in range(1, n+1):
        total_xor ^= dfs(i, -1)

    if total_xor == 0:
        return "YES"
    else:
        return "NO"

print(solve())
