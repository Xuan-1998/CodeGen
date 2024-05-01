import heapq

n, m = map(int, input().split())
dp = [[float('inf')] * (m + 1) for _ in range(n)]

graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    graph.setdefault(u, []).append(v)

k = int(input())
path = list(map(int, input().split()))

pq = []
heapq.heappush(pq, (0, 0))  # Start with the first vertex of the path
for i in range(k - 1):
    _, p = heapq.heappop(pq)
    dp[p][i + 1] = min(dp[p][i], dp[p][k])
    for neighbor in graph.get(path[i], []):
        if neighbor == path[i + 1]:
            heapq.heappush(pq, (dp[p][i], neighbor))
        else:
            heapq.heappush(pq, (min(dp[p][i], dp[p][k]) + 1, neighbor))

max_count = 0
for i in range(k):
    max_count = max(max_count, dp[path[i]][k])

print(min(map(lambda x: x[0], pq)), max_count)
