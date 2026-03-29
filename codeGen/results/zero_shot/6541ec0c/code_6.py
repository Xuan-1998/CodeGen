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

    xor_values = {}
    current_xor = 0

    for node in sorted(values):
        if node not in xor_values:
            xor_values[node] = current_xor
            current_xor ^= node
        else:
            if xor_values[node] != current_xor:
                return "NO"
            current_xor ^= node

    return "YES" if len(xor_values) <= k else "NO"

t = int(input())
for _ in range(t):
    print(solve())
