n = int(input())
m = int(input())
T = int(input())

edges = []
for _ in range(m):
    u, v, t = map(int, input().split())
    edges.append((u, v, t))

graph = {i: [] for i in range(1, n + 1)}
for u, v, t in edges:
    graph[u].append((v, t))

dp = {i: -float('inf') for i in range(1, n + 1)}

for v in range(1, n + 1):
    for u, w in graph[v]:
        if dp[u] + w <= T:
            dp[v] = max(dp[v], dp[u] + w)

k = 0
while n > 1 and dp[n] <= T:
    k += 1
    n -= 1

print(k)
print(*range(1, k + 2), sep='\n')
