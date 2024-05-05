from collections import deque

n, m, T = map(int, input().split())
graph = [[] for _ in range(n + 1)]
dp = [[0] * (T + 1) for _ in range(n + 1)]

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

q = deque([(n, T)])
while q:
    i, t = q.popleft()
    if dp[i][t] > 0:
        continue
    for j, edge_t in graph[i]:
        if edge_t <= t:
            dp[j][t - edge_t] = max(dp[j][t - edge_t], dp[i][t - edge_t] + 1)
            q.append((j, t - edge_t))

print(dp[1][T])
for i in range(T, 0, -1):
    if dp[1][i] > 0:
        print(1, end=' ')
        break
while True:
    for j, edge_t in graph[1]:
        if edge_t <= i and dp[j][i - edge_t] > 0:
            print(j + 1, end=' ')
            break
    i -= 1
print()
