import sys

n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edges.append((u, v))

edges.sort(key=lambda x: abs(x[0] - x[1]))

dp = [0] * (n + 1)
for edge in edges:
    u, v = edge
    dp[v] = max(dp[v], dp[u] + 1)

tail_len = max(dp)

spine_count = 0
for edge in edges:
    u, v = edge
    if dp[u] + 1 != dp[v]:
        spine_count += 1

beauty = tail_len * spine_count
print(beauty)
