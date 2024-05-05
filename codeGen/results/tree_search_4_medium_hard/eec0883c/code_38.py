import sys
from collections import deque

n = int(sys.stdin.readline().strip())
w = list(map(int, sys.stdin.readline().split()))
graph = {}
for _ in range(n - 1):
    u, v, c = map(int, sys.stdin.readline().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append((v, c))
    graph[v].append((u, c))

dp = [[0] * (10**9 + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
max_gas_available = max(w)

for i in range(1, n + 1):
    if not visited[i]:
        queue = deque([(i, w[i - 1])])
        visited[i] = True
        while queue:
            city, gas = queue.popleft()
            for neighbor, road_length in graph[city]:
                new_gas = min(gas - road_length, max_gas_available)
                if not visited[neighbor] or dp[neighbor][new_gas] < new_gas:
                    dp[neighbor][new_gas] = new_gas
                    queue.append((neighbor, new_gas))
        for j in range(max_gas_available + 1):
            dp[i][j] = min(dp[i - 1][min(j - road_length, max_gas_available)] for road_length in graph.get(i, []))

print(max(dp[-1]))
