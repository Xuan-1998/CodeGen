import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [float('inf')] * (n + 1)
path = list(map(int, input().split()))

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

q = [(0, n)]  # Initialize queue with the last node and distance 0

while q:
    d, node = heapq.heappop(q)
    if dp[node] <= d:  # If we've already found a shorter path to this node, skip it
        continue
    dp[node] = d
    for neighbor in graph[node]:
        nd = d + 1  # Recompute the shortest distance from this node to t
        if nd < dp[neighbor]:  # Update the shortest distance to this neighbor
            dp[neighbor] = nd
            heapq.heappush(q, (nd, neighbor))

min_recomputations = float('inf')
max_recomputations = 0
for i in range(1, len(path)):
    min_recomputations = min(min_recomputations, dp[path[i]] - dp[path[i - 1]])
    max_recomputations = max(max_recomputations, dp[path[i]] - dp[path[i - 1]])

print(f"{min_recomputations} {max_recomputations}")
