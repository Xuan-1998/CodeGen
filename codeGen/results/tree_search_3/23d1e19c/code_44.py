import sys

def read_input():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    k = int(input())
    path = list(map(int, input().split()))
    return n, m, edges, k, path

def has_edge(edges, u, v):
    for edge in edges:
        if (edge[0] == u and edge[1] == v) or (edge[0] == v and edge[1] == u):
            return True
    return False

n, m, edges, k, path = read_input()
dp = [float('inf')] * n

for i in range(n):
    for j in range(min(path), i+1):
        if has_edge(edges, j, i):
            dp[i] = min(dp[i], dp[j] + 1)

min_recomputations = float('inf')
max_recomputations = 0
for i in range(n):
    min_recomputations = min(min_recomputations, dp[i])
    max_recomputations = max(max_recomputations, dp[i])

print(min_recomputations, max_recomputations)
