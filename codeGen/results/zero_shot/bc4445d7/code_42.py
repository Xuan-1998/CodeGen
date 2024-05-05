import sys

n = int(sys.stdin.readline())
edges = []
for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))
m = int(sys.stdin.readline())
prime_factors = list(map(int, sys.stdin.readline().split()))
k = prime_factors[0]
for p in prime_factors[1:]:
    k *= p

from collections import defaultdict

graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

def f(i, j):
    visited = [False] * (n + 1)
    path_sum = 0
    stack = [(i, i)]
    while stack:
        u, prev_u = stack.pop()
        if not visited[u]:
            visited[u] = True
            path_sum += next((v for v in graph[u] if v != prev_u), None)
            if u == j:
                return path_sum
            for v in graph[u]:
                if not visited[v]:
                    stack.append((v, u))
    return 0

max_distribution_index = sum(sum(f(i, j)) for i in range(n) for j in range(i + 1, n)) % (10**9 + 7)
print(max_distribution_index)
