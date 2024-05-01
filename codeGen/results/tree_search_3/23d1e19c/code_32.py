from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

k = int(input())
path = list(map(int, input().split()))

dp = [0] * (n + 1)
q = deque([path[-1]])

while q:
    t = q.popleft()
    for i in range(k - 2, -1, -1):
        if graph[path[i]][0] == t:
            dp[t] = max(dp[t], dp[path[i]] + 1)
            q.append(graph[path[i]][0])
            break

print(min(dp), max(dp))
