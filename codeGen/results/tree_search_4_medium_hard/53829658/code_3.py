import sys
from collections import defaultdict, deque

n = int(input())
graph = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  # for undirected tree

dp = [float('inf')] * (n + 1)
parent = [-1] * (n + 1)

dp[1] = 0

queue = deque([(1, 0)])  # node, distance
while queue:
    node, dist = queue.popleft()
    for neighbor in graph[node]:
        if dp[neighbor] > dist + 1:
            dp[neighbor] = dist + 1
            parent[neighbor] = node
            queue.append((neighbor, dist + 1))

capital_cities = []
for i in range(2, n + 1):
    capital_cities.append(parent[i])

print(min(dp[2:]))
print(*capital_cities)
