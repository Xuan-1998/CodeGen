from collections import deque

n, m, T = map(int, input().split())
graph = [[] for _ in range(n+1)]
dp = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))

q = deque([(1, n-1, 0)])
while q:
    s, e, t = q.popleft()
    if dp[s][e] == 0 or t <= T:
        for v, w in graph[s]:
            if dp[v][e] < dp[s][e-1] + 1 and w <= T - (e-s):
                dp[v][e] = max(dp[v][e], dp[s][e-1] + 1)
                q.append((v, e, t+w))
        if s == 1:
            print(max(j for i in range(n+1) for j in range(n+1) if dp[i][j]))
    else:
        break

for i in range(2, n):
    if dp[1][i] > 0:
        print(i)
